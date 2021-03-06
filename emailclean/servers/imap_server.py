from imaplib import IMAP4_SSL, IMAP4
from emailclean.database.SQLite_database import ENGINE
from emailclean.database.SQLite_database import SqliteSession, SqlliteSessionMaker
from sqlalchemy.orm.session import Session, sessionmaker
import email
import re


MSG_FLAGS_RE_DICT= {
    'localhost': r'FLAGS r\((?P<FLAGS>.*?)\)',
    'imap.gmail.com': r'FLAGS \((?P<FLAGS>.*?)\)'
}

UID_RE_DICT= {
    'localhost': r"UID\s(?P<UID>\d+)",
    'imap.gmail.com': r"UID\s(?P<UID>\d+)"
}
# re string for extracting flags from PERMANENTFLAGS response code
SERVER_FLAGS_RE_DICT={
    'localhost': r'\[A-Za-z]*',
    'imap.gmail.com': r'\\[A-Za-z]*'
}
#supported flags


class ImapClient():

    # conn_dict is validated as a dict buy request object. so no need
    # to validate here
    def __init__(self, conn_dict, connection):
        self.conn_dict = conn_dict
        self.connection = connection




    @classmethod
    def connect(cls, conn_dict):
        """
        Connects to a imap server. SSL should be True if connecting via a SSL
       connection

        :return: a ImapClient object with a imaplib.Imap connection and a
        """
        #TODO add in google API here, more secure i think
        host = conn_dict.get('host')
        port = conn_dict.get('port')
        email = conn_dict.get('email')
        password = conn_dict.get('password')
        mailbox = conn_dict.get('mailbox')
        SSL = conn_dict.get('SSL')
        try:
            if SSL is False:
                connection = IMAP4(host=host, port=port)
            else:
                connection = IMAP4_SSL(host=host, port=port)
        except Exception as e:
            raise e
        connection.login(email, password)
        connection.select(mailbox=mailbox)

        return cls(conn_dict, connection)


    def fetch(self, mailbox):
        """
        execute a fetch command for all UIDs in mailbox, as follows
        (FLAGS BODY.PEEK[HEADER.FIELDS (DATE FROM SUBJECT)])
        :param mailbox: str: name on mailbox. ie 'inbox' or 'sent'
        :return: a list of email.Email objects
        """
        try:
            self.connection.select(mailbox=mailbox)
            result, data = self.connection.uid('FETCH', '1:*', '(FLAGS BODY.PEEK[HEADER.FIELDS (DATE FROM SUBJECT)])')
            msg_list = []
            for index in range(0, len(data), 2):
                # add a mailbox_name columns

                fields_str = data[index][0].decode("utf-8") + data[index + 1].decode("utf-8")
                email_obj = email.message_from_bytes(data[index][1])
                email_obj.__setitem__('mailbox', mailbox)
                email_obj.__setitem__('uid', self._get_UID(fields_str))
                email_obj.__setitem__('flags', self._get_flags(fields_str))
                if "Seen" in email_obj['flags']:
                    email_obj.__setitem__('read', True)
                else:
                    email_obj.__setitem__('read', False)
                msg_list.append(email_obj)
        except Exception as e:
            raise e

        return msg_list

    def delete(self, mailbox):

        """
        expunge mailbox. messages to be deleted must have been flagged
        in the db, and flags updated on the imap server before this method is called
        otherwise it will raise an ValueError Exception
        :param mailbox: str: name on mailbox. ie 'inbox' or 'sent'
        :return: a list of UIDs that have been deleted
        """
        try:
            print("Removing messages on remote server")
            #todo check lengh of mailbox as a before
            self.connection.select(mailbox=mailbox)
            result, data = self.connection.expunge()
            #TODO return new length of mailbox as an after, so return no of emails deleted
        except Exception as e:
            raise e
        return data

    def mark_as(self, mailbox:str, UIDs:list, flags=None, replace_flags=True):
        """
        Replace all flags in message with flags in flags string. This function can be used to update all flags for a
        given list of UIDs. In which case the flag strings are taken from the db. it can also be used to update
        flags to a new string by passing a string in the flags argument
        :param mailbox: name on mailbox. ie 'inbox' or 'sent'
        :param flags: string of flags to be added.if ommited, flags will be updated directly from database. Note all
        flags are replaced
        :param UIDs: list of message UIDs that flag will be added to
        :param replace_flags: if true flags on server are replaced. if false flags on server are appended to with new
        flag string. note no checks are carried out to see if email already has flag. ie it is possible to add
        "\seen' to a email that already has the "\seen" flag. this might cause trouble.
        :returns a list of (UID, Flags_set) tuples
        """

        return_list = []

        def update_flags(uid, flag_str):
            # 'FLAGS' is used instead of '+FLAGS' to prevent the need
            # to maintain info on which emails have had which flags changed
            # all flags are always replaced with flags presented

            #result, data = self.connection.store(str(uid).encode(), 'FLAGS', flags.lstrip())

            result, data = self.connection.uid('store', str(uid), 'FLAGS', flag_str.lstrip())

            if data[0]:
                #TODO make this more of a logging feature
                return_data = data[0].decode()
            else:
                # TODO make this more of a logging feature
                #TODO if you get a NoneType returned, ping the server again for the msg details and return to user.

                print(f"none type detected {uid}, result: {result}, data: {data}")
                return_data = flag_str
            return_list.append((uid, return_data))


        try:
            self.connection.select(mailbox=mailbox)

            if not flags:
                """ this breaks the flow for a clean architecture. if you change your db then this method will
                have to change also. you need to work out a way to call session.get directly. Note also, this test
                passes as you have mocked the get command. however SQLalchemy might not like this behavour."""
                session_mkr = SqlliteSessionMaker()
                session = session_mkr()
                email_dict = session.get(get="all")
                print(f"No flags received, Updating flags from database")
                for email in email_dict.get(mailbox):
                    if len(email.flags) > 1:
                        update_flags(email.uid, email.flags)
            else:
                print(f"flags found Updating flags for {len(UIDs)} emails")
                for uid in UIDs:
                    update_flags(uid, flags)
        except Exception as e:
            raise e
        return return_list

    def new_mb(self, mailbox:str):
        """
        create a new mailbox on the server. use to create chrildren boxes also
        ie 'higherMailBox/subMailBox'
        :param mailbox: Name for new mailbox
        :return: ValueError if name already in use, otherwise 'Success'
        """
        try:
            result, data = self.connection.create(mailbox)
            if result != 'OK':
                raise ValueError('Could not create mailbox, name probably already exists')
        except Exception as e:
            raise e
        return 'Success'

    def move_to(self, mailbox:str, UIDs:list):
        #TODO add this functionality to the comand line. ie 100 emails from.... delete? or move to?
        """

        :param mailbox: Name for destination mailbox. include parent mailboxes also
        ie 'higherMailBox/subMailBox'
        :param UIDs: list of message UIDs that will be moved
        :return: a list of (UID, destination) tuples. a Value error is raised
        if destination mailbox does not exist
        """
        return_list = []
        try:
            for uid in UIDs:
                #this will probably have to be a uid command, as copy requires a message set
                # result,date = self.connection.uid('copy', str(uid), mailbox) should work
                result, data = self.connection.copy(str(uid).encode(), mailbox)
                if result != 'OK':
                    raise ValueError(f'move unsuccessful, check {mailbox} exists. '
                                     f'Use connection.new_mb to create new mailbox')
                return_data = data[0].decode()
                return_list.append((uid, return_data))
        except Exception as e:
            raise e
        return return_list

    def supported_flags(self):
        """
        get a list of flags that client can change permanently
        :return: a list of flag strings. ie \\Answered
        """
        result = self.connection.response('PERMANENTFLAGS')
        flags_str = result[1][0].decode()
        match = re.findall(SERVER_FLAGS_RE_DICT[self.conn_dict.get('host')], flags_str)
        return match

    def _get_flags(self, fields_str:str):
        """
        return flags given a string from imap server
        :param flag_str: the string returned from the imap server
        :return: a string with flags seperated  ie "\\Seen \\ Answered \\Deleted"
        """
        regex = re.compile(MSG_FLAGS_RE_DICT[self.conn_dict.get('host', 'default')])
        match = regex.search(fields_str)

        if match:
            return match.groups('FLAGS')[0]
        else:
            return ""

    def _get_UID(self, fields_str):
        """
        get unique id from imap Fetch response
        :param fields_str: the byte string returned from the imap server
        :return: a string rep of an intiger
        """
        regex = re.compile(UID_RE_DICT[self.conn_dict.get('host', 'default')])
        match = regex.search(fields_str)
        if match:
            return match.group('UID')
        else:
            return None






