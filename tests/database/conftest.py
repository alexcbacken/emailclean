import pytest
from emailclean.domain.email import Email
from emailclean.database.SQLite_objects import Base, email
import sqlalchemy
import sqlite3
from sqlalchemy.orm import sessionmaker

def SQLite_is_responsive():
    # return true if SQLite can be connected to.
    try:
        conn = sqlite3.connect(':memory:')
        conn.close()
        return True
    except Exception as e:
        print(e)
        return False


@pytest.fixture
def SQLite_data():
    # return a list of email objects
    email_1 = Email(
        uid=1,
        sender="alex backen <alexcbacken@gmail.com>",
        date="Sun, 05 Apr 2020 19:28:21 +0000",
        subject="a test email subject",
        receiver="email_clean@gmail.com",
        read=True,
        flags="//Seen",
        mailbox='inbox')

    email_2 = Email(
        uid=2,
        sender="Daily Beast: Scouted <emails@thedailybeast.com>",
        date="Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        subject="Welcome to Scouted!",
        receiver="email_clean@gmail.com",
        read=True,
        flags="//Seen",
        mailbox='inbox')

    email_3 = Email(
        uid=3,
        sender="Morning Brew <crew@morningbrew.com>",
        date="Sun, 5 Apr 2020 19:35:51 +0000 (UTC)",
        subject="Caution: Morning Brew coming in hot",
        receiver="email_clean@gmail.com",
        read=False,
        flags="//Seen",
        mailbox='inbox')

    email_4 = Email(
        uid=4,
        sender="Vox Sentences <newsletter@vox.com>",
        date="Tue, 07 Apr 2020 08:00:38 +1000",
        subject="Rotten masks and shared ventilators",
        receiver="email_clean@gmail.com",
        read=True,
        flags=r"/Answered",
        mailbox='inbox')

    email_5 = Email(
        uid=5,
        sender="Vox Sentences <newsletter@vox.com>",
        date="Mon, 06 Apr 2020 19:02:02 -0400",
        subject="Trump Removes Watchdog for $2T Virus Bill From Post",
        receiver="email_clean@gmail.com",
        read=False,
        flags="",
        mailbox='inbox')


    email_6 = Email(
        uid=6,
        sender="Alex Backen <alexcbacken@gmail.com>",
        date="Mon, 06 Apr 2020 15:44:42 +0000 (UTC)",
        subject="the times alone are the times alone",
        receiver="email_clean@gmail.com",
        read=True,
        flags="",
        mailbox='inbox')

    email_7 = Email(
        uid=7,
        sender="Alex Backen <alexcbacken@gmail.com>",
        date="Thu, 06 Apr 2020 15:44:42 +0000 (UTC)",
        subject="something for everyone",
        receiver="email_clean@gmail.com",
        read=True,
        flags="",
        mailbox='inbox')
    return [email_1,email_2,email_3,email_4,email_5,email_6, email_7]

@pytest.fixture()
def mybox_email_list():
    return [
        {"uid":1,
        "sender":"alex backen <alexcbacken@gmail.com>",
        "date":"Sun, 05 Apr 2020 19:28:21 +0000",
        "subject":"a test email subject",
        "receiver":"email_clean@gmail.com",
        "read":True,
         "flags":"//seen",
         "mailbox":"mybox"},
        {"uid":2,
         "sender": "Vox Sentences <newsletter@vox.com>",
        "date":"Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        "subject":"Welcome to Scouted!",
        "receiver":"email_clean@gmail.com",
        "read":True,
        "flags":"//seen",
         "mailbox":"mybox"},
    {"uid":3,
        "sender":"Morning Brew <crew@morningbrew.com>",
        "date":"Sun, 5 Apr 2020 19:35:51 +0000 (UTC)",
        "subject":"Caution: Morning Brew coming in hot",
        "receiver":"email_clean@gmail.com",
        "read":False,
    "flags":"//seen",
     "mailbox":"mybox"},
        {"uid":4,
        "sender":"Vox Sentences <newsletter@vox.com>",
        "date":"Tue, 07 Apr 2020 08:00:38 +1000",
        "subject":"Rotten masks and shared ventilators",
        "receiver":"email_clean@gmail.com",
        "read":True,
        "flags":"//seen",
         "mailbox":"mybox"},
        {"uid":5,
        "sender":"Vox Sentences <newsletter@vox.com>",
        "date":"Mon, 06 Apr 2020 19:02:02 -0400",
        "subject":"Trump Removes Watchdog for $2T Virus Bill From Post",
        "receiver":"email_clean@gmail.com",
        "read":False,
        "flags":"//seen",
         "mailbox":"mybox"},
        {"uid": 6,
         "sender": "Alex Backen <alexcbacken@gmail.com>",
         "date": "Mon, 06 Apr 2020 15:44:42 +0000 (UTC)",
         "subject": "the times alone are the times alone",
         "receiver": "email_clean@gmail.com",
         "read": False,
         "flags": "//seen",
         "mailbox":"mybox"},
        {"uid": 7,
         "sender": "Alex Backen <alexcbacken@gmail.com>",
         "date": "Thu, 06 Apr 2020 15:44:42 +0000 (UTC)",
         "subject": "something for everyone",
         "receiver": "email_clean@gmail.com",
         "read": False,
         "flags": "//seen",
         "mailbox":"mybox"}
        ]

@pytest.fixture()
def inbox_email_list():
    return [
        {"uid":1,
        "sender":"alex backen <alexcbacken@gmail.com>",
        "date":"Sun, 05 Apr 2020 19:28:21 +0000",
        "subject":"a test email subject",
        "receiver":"email_clean@gmail.com",
        "read":True,
         "flags":"//seen",
         "mailbox":"inbox"},
        {"uid":2,
         "sender": "Vox Sentences <newsletter@vox.com>",
        "date":"Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        "subject":"Welcome to Scouted!",
        "receiver":"email_clean@gmail.com",
        "read":True,
        "flags":"//seen",
         "mailbox":"inbox"},
    {"uid":3,
        "sender":"Morning Brew <crew@morningbrew.com>",
        "date":"Sun, 5 Apr 2020 19:35:51 +0000 (UTC)",
        "subject":"Caution: Morning Brew coming in hot",
        "receiver":"email_clean@gmail.com",
        "read":False,
    "flags":"//seen",
     "mailbox":"inbox"},
        {"uid":4,
        "sender":"Vox Sentences <newsletter@vox.com>",
        "date":"Tue, 07 Apr 2020 08:00:38 +1000",
        "subject":"Rotten masks and shared ventilators",
        "receiver":"email_clean@gmail.com",
        "read":True,
        "flags":"//seen",
         "mailbox":"inbox"},
        {"uid":5,
        "sender":"Vox Sentences <newsletter@vox.com>",
        "date":"Mon, 06 Apr 2020 19:02:02 -0400",
        "subject":"Trump Removes Watchdog for $2T Virus Bill From Post",
        "receiver":"email_clean@gmail.com",
        "read":False,
        "flags":"//seen",
         "mailbox":"inbox"},
        {"uid": 6,
         "sender": "Alex Backen <alexcbacken@gmail.com>",
         "date": "Mon, 06 Apr 2020 15:44:42 +0000 (UTC)",
         "subject": "the times alone are the times alone",
         "receiver": "email_clean@gmail.com",
         "read": False,
         "flags": "//seen",
         "mailbox":"inbox"},
        {"uid": 7,
         "sender": "Alex Backen <alexcbacken@gmail.com>",
         "date": "Thu, 06 Apr 2020 15:44:42 +0000 (UTC)",
         "subject": "something for everyone",
         "receiver": "email_clean@gmail.com",
         "read": False,
         "flags": "//seen",
         "mailbox":"inbox"}
        ]


@pytest.fixture(scope='session')
def SQLite_engine():
    # return a empty SQlite db

    if SQLite_is_responsive():
        engine = sqlalchemy.create_engine('sqlite://')

        with engine.connect():

            yield engine


@pytest.fixture(scope='session')
def SQLite_session_empty(SQLite_engine):

    Base.metadata.create_all(SQLite_engine)

    Base.metadata.bind = SQLite_engine

    Session = sessionmaker(bind=SQLite_engine)

    session = Session()

    yield session

    session.close()


@pytest.fixture(scope='function')
def SQLite_session(SQLite_data,SQLite_session_empty):
    # return a populated SQLlite db


    for em in SQLite_data:
        SQLite_session_empty.add(em)
        SQLite_session_empty.commit()

    yield SQLite_session_empty

    # delete all the rows, but not the table
    SQLite_session_empty.query(email).delete()
