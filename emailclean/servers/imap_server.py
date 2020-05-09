from imaplib import IMAP4_SSL, IMAP4
import email
import re


FLAGS_RE_DICT= {
    'localhost': r'FLAGS \((?P<FLAGS>.*?)\)',
    'imap.gmail.com': r'FLAGS \((?P<FLAGS>.*?)\)'
}

UID_RE_DICT= {
    'localhost': r"UID\s(?P<UID>\d+)",
    'imap.gmail.com': r"UID\s(?P<UID>\d+)"
}

class ImapClient():

    # conn_dict is validated as a dict buy request object. so no need
    # to validate here
    def __init__(self, conn_dict, connection):
        self.conn_dict = conn_dict
        self.connection = connection

    @classmethod
    def connect(cls, conn_dict):
        """
        Connects to a imap server. SSL shoul dbe True is connecting via a SSL
       connection

        :return: a ImapClient object with a imaplib.Imap connection and a
        """
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
                fields_str = data[index][0].decode("utf-8") + data[index + 1].decode("utf-8")
                email_obj = email.message_from_bytes(data[index][1])
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

    def _get_flags(self, fields_str):
        """
        return flags given a byte string from imap server
        :param flag_str: the string returned from the imap server
        :return: a string with flags seperated by "~" ie "Seen~Answered~deleted"
        """
        regex = re.compile(FLAGS_RE_DICT[self.conn_dict.get('host', 'default')])
        match = regex.search(fields_str)
        flags = match.groups('FLAGS')[0]
        if flags:
            return flags[1:].replace(r"\\", "~")
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






