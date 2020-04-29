import pytest
import imaplib, threading, sys, localmail_imap
from os import path
from twisted.logger import Logger, textFileLogObserver

pytestmark = pytest.mark.imap_server

HOST = 'imap.gmail.com'
EMAIL = 'someemail@gmail.com'
PASSWORD = "somepassword"
MAILBOX = "INBOX"

@pytest.fixture(scope='function')
def imap_mock():
    observer = textFileLogObserver(sys.stdout)
    logStdout = Logger(observer=observer)

    thread = threading.Thread(
        target=localmail_imap.run,
        args=(2025, 2146, 8880, path.abspath('emailclean.mbox'))
)
    thread.start()

    with imaplib.IMAP4(host='localhost', port=2146) as M:
        M.login(EMAIL, PASSWORD)
        M.select(mailbox="INBOX")
        result, data = M.uid('FETCH', '1:*', '(FLAGS BODY.PEEK[HEADER.FIELDS (DATE FROM SUBJECT)])')
        logStdout.debug(f"search complete, {len(data)} messages found")

    localmail_imap.shutdown_thread(thread)

    return result, data

@pytest.fixture(scope='session')
def mbox_mails():
    pass
    #fixture to return hard wired mail box for testing purposes










