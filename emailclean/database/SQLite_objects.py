from sqlalchemy import Column, Integer, String, Boolean, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
# the declaratiuve base is the base class for all SQLAlchemy objects.
# your email object inherists from this class. and is mapped to the table
# "emails"
# from this class SQLAlchemy will create the table "emails" add add it to the
# email._table_ attribute.

class email(Base):
    __tablename__ = 'emails'

    mailbox = Column(String, primary_key=True)
    uid = Column(Integer, primary_key=True)
    sender = Column(String)
    date = Column(String)
    subject = Column(String)
    receiver = Column(String)
    read = Column(Boolean)
    flags = Column(String)


    @classmethod
    def from_dict(cls, dict):
        cls.uid = dict["uid"]
        cls.sender = dict["sender"]
        cls.date = dict["date"]
        cls.subject = dict["subject"]
        cls.receiver = dict["receiver"]
        cls.read = dict["read"]
        cls.flags = dict["flags"]
        cls.mailbox = dict["mailbox"]
        return cls(uid=cls.uid,
                   sender=cls.sender,
                   date=cls.date,
                   subject=cls.subject,
                   receiver=cls.receiver,
                   read=cls.read,
                   flags=cls.flags,
                   mailbox=cls.mailbox)






