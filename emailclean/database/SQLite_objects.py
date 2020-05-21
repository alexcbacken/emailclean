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


def render_emails(messages):
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








