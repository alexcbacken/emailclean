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
        try:
            return cls(mailbox=dict["mailbox"],
                       uid=dict["uid"],
                       sender=dict["from"],
                       date=dict["date"],
                       subject=dict["subject"],
                       receiver=dict["receiver"],
                       read=dict["read"],
                       flags=dict["flags"])
        except KeyError:
            return cls(mailbox=dict["mailbox"],
                       uid=dict["uid"],
                       # some hosts use 'sender' instead of 'from'
                       sender=dict["sender"],
                       date=dict["date"],
                       subject=dict["subject"],
                       receiver=dict["receiver"],
                       read=dict["read"],
                       flags=dict["flags"])

    @classmethod
    def from_email_domain_obj(cls, email_obj):
        return cls(mailbox=email_obj.mailbox,
                   uid=email_obj.uid,
                   sender=email_obj.sender,
                   date=email_obj.date,
                   subject=email_obj.subject,
                   receiver=email_obj.receiver,
                   read=email_obj.read,
                   flags=email_obj.flags)










