import pytest
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

@pytest.fixture(scope='session')
def mbox_mails():
    pass
    #fixture to return hard wired mail box for testing purposes










