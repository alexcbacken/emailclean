from emailclean.database.SQLite_objects import Base, email
from sqlalchemy import create_engine, func
from sqlalchemy.orm.session import Session, sessionmaker

ENGINE = create_engine('sqlite://')
Base.metadata.create_all(ENGINE)
Base.metadata.bind = ENGINE


class SqliteSession(Session):

    """
     A SQL-Alchemy Session object. Bound to an in-memory SQLite Database. Note there is no SessionMaker as
     we will never need more than one session per engine, due the linear nature of

     :return: a SqliteDataBase object, which is actually a SQLAlchemy Session object
     """


    def create(self, messages:list):
        """
        Populate the DataBase, with email.EMail objects, as returned by a request to an IMAP server.
        :param messages: a list of email.EMail objects
        :param name: the name of inbox
        :return: "success"
        """
        try:
            self.add_all([email.from_dict(msg) for msg in messages])
            self.commit()
        except Exception as e:
            raise e
        return "Success"

    def mark_as(self, uids, mailbox, flags):
        """
        Mark the emails with <uid> in <mailbox> with <flags>
        :param uids: a list of unique identifiers
        :param mailbox: a string corresponding to the name of the mailbox, the emails are in
        :param flags: a list of flag strings strings ie [seen, deleted, answered]
        """

        try:

            result = self.query(email).filter(email.mailbox == mailbox, email.uid.in_(uids)).update(
                {'flags': flags},
                synchronize_session=False)
            self.commit()
        except Exception as e:
            raise e
        return result

    def get(self, get='by_sender'):
        """
        gets a dictionary of emails organised by sender.  marked for deletion, or all email currently loaded
        emails sent by each sender in each mailbox
        :param get: accepted values: by_sender, all, deleted
        :param mailbox.
        :return: a dictionay. key is name of mailbox. value is a list of tuple pairs (count, sender). with 'count'
        being the number of emails from 'sender'. if 'all' is used, then values are lists of email objects.
        """

        def make_dict(sender_query, distinct_sender):
            return_dict = {}
            for sender in distinct_sender.all():

                emails = sender_query.filter(email.sender == sender[0]).subquery()
                sender_count = (self.query(func.count(emails.c.sender)).scalar(), sender[0])

                emails_mailbox = self.query(emails.c.mailbox).distinct().all()

                for mailbox in emails_mailbox:
                    if mailbox[0] in return_dict:
                        return_dict[mailbox[0]].append(sender_count)
                    else:
                        return_dict.update({mailbox[0]: [sender_count, ]})
            return return_dict

        try:
            if get == "by_sender":
                sender_query = self.query(email.sender, email.mailbox)
                distinct_sender = self.query(email.sender).distinct()
                return make_dict(sender_query, distinct_sender)

            elif get == "all":
                return_dict = {}
                mailbox_list = self.query(email.mailbox).distinct().all()
                for mbox in mailbox_list:
                    # add to dict: mailbox name as key, list of email objects as value
                    return_dict.update({mbox[0]: self.query(email).filter(email.mailbox == mbox[0]).all()})

                return return_dict

            elif get == "deleted":

                deleted_query = self.query(email.sender, email.mailbox).filter(email.flags.like('%deleted%'))
                distinct_deleted_sender = self.query(deleted_query.subquery().c.sender).distinct()
                return make_dict(deleted_query, distinct_deleted_sender)

        except Exception as e:
            raise e

    def get_uids(self, paramater):
        pass

class SqlliteSessionMaker(sessionmaker):
    """
    A SQLAlchemy session maker, that returns the custom, SqliteSession session object.
    """
    def __init__(self,):
        super().__init__(bind=ENGINE,class_=SqliteSession)




