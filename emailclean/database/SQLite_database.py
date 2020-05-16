from emailclean.domain.email import Email
from emailclean.database.SQLite_objects import Base
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm.session import Session, sessionmaker
from sqlalchemy.orm import mapper
from sqlalchemy.exc import ArgumentError


ENGINE = create_engine('sqlite://')

Base.metadata.create_all(ENGINE)
Base.metadata.bind = ENGINE



class SqliteSession(Session):

    """
     A SQL-Alchemy Session object. Bound to an in-memory SQLite Database. Note there is no SessionMaker as
     we will never need more than one session per engine, due the linear nature of

     :return: a SqliteDataBase object, which is actually a SQLAlchemy Session object
     """


    def create(self, messages:list, name:str):
        """
        Populate the DataBase, with email.EMail objects, as returned by a request to an IMAP server.
        :param messages: a list of email.EMail objects
        :param name: the name of inbox
        :return: "success"
        """
        try:
            mailbox = self.get_table(name)
            try:
                mapper(Email, mailbox)
            except ArgumentError:
                pass
            # this should now just add the details to the same db

            mailbox.create()
            self.add_all([Email.from_dict(msg) for msg in messages])
            self.commit()
        except Exception as e:
            raise e
        return "Success"








class SqlliteSessionMaker(sessionmaker):
    """
    A SQLAlchemy session maker, that returns the custom, SqliteSession session object.
    """
    def __init__(self,):
        super().__init__(bind=ENGINE,class_=SqliteSession)




