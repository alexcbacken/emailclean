from emailclean.database.SQLite_objects import Base, email
from emailclean.domain. email import Email
from sqlalchemy import create_engine
from sqlalchemy.orm.session import Session, sessionmaker


ENGINE = create_engine('sqlite://')
#ENGINE = create_engine('sqlite:///C:\\Users\\Alex\\PycharmProjects\\sql2.db', echo=True)
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
            self.add_all(self.render_emails(messages))
            self.commit()
        except Exception as e:
            raise e
        return "Success"

    def render_emails(self, messages):
        email_list = []
        for msg in messages:
            email_list.append(email(mailbox=msg["mailbox"],
                                    uid=msg["uid"],
                                    sender=msg["sender"],
                                    date=msg["date"],
                                    subject=msg["subject"],
                                    receiver=msg["receiver"],
                                    read=msg["read"],
                                    flags=msg["flags"]))
        return email_list




class SqlliteSessionMaker(sessionmaker):
    """
    A SQLAlchemy session maker, that returns the custom, SqliteSession session object.
    """
    def __init__(self,):
        super().__init__(bind=ENGINE,class_=SqliteSession)




