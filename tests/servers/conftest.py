import pytest
from emailclean.database.SQLite_objects import email
import threading, sys
from os import path, remove
from twisted.logger import Logger, textFileLogObserver
from mailbox import mbox
import localmail_imap



pytestmark = pytest.mark.imap_server

HOST = 'imap.gmail.com'
EMAIL = 'someemail@gmail.com'
PASSWORD = "somepassword"
MAILBOX = "INBOX"


# set this up so you do a set up and tear down, so you can shut down
# your thread
"""
pytest supports execution of fixture specific finalization code when 
the fixture goes out of scope. By using a yield statement instead of 
return, all the code after the yield statement serves as the 
teardown code:
"""




@pytest.fixture()
def connection_dict():
    return {'host':'localhost',
            'port': 2147,
            'email' : 'someemail@gmail.com',
            'password' : "somepassword",
            'mailbox': "INBOX",
            'SSL': False}

# start imap server on local host




# a test must take imap_mock as an argument, for this to be run
"""
@pytest.fixture(scope='function')
def set_mailbox():

    # set up mbox file
    mb = mbox('test_inbox.mbox')
    mb_temp = mbox(next(NAME_GEN))
    for msgs in mb.items():
        mb_temp.add(msgs[1])
    mb.close()
    mb_temp.close()
    return mb_temp._path
    localmail_imap.imap.INBOX.setFile()

    
    with imaplib.IMAP4(host='localhost', port=2146) as M:
        M.login(EMAIL, PASSWORD)
        M.select(mailbox="INBOX")
        result, data = M.uid('FETCH', '1:*', '(FLAGS BODY.PEEK[HEADER.FIELDS (DATE FROM SUBJECT)])')
        logStdout.debug(f"search complete, {len(data)} messages found")

    yield imaplib.IMAP4
    """

@pytest.fixture
def email_objects():
    # return a list of SQLite_objects.email objects
    return {"inbox":[
            email(uid=1,
                  sender="alex backen <alexcbacken@gmail.com>",
                  date="Sun, 05 Apr 2020 19:28:21 +0000",
                  subject="a test email subject",
                  receiver="email_clean@gmail.com",
                  read=True,
                  flags="\\Seen",
                  mailbox='inbox'),
            email(
                  uid=2,
                  sender="Daily Beast: Scouted <emails@thedailybeast.com>",
                  date="Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
                  subject="Welcome to Scouted!",
                  receiver="email_clean@gmail.com",
                  read=True,
                  flags="\\Seen",
                  mailbox='inbox'),
            email(
                  uid=3,
                  sender="Morning Brew <crew@morningbrew.com>",
                  date="Sun, 5 Apr 2020 19:35:51 +0000 (UTC)",
                  subject="Caution: Morning Brew coming in hot",
                  receiver="email_clean@gmail.com",
                  read=False,
                  flags="\\Seen",
                  mailbox='inbox'),
            email(
                  uid=4,
                  sender="Vox Sentences <newsletter@vox.com>",
                  date="Tue, 07 Apr 2020 08:00:38 +1000",
                  subject="Rotten masks and shared ventilators",
                  receiver="email_clean@gmail.com",
                  read=True,
                  flags="\\Answered",
                  mailbox='inbox')

         ]}












