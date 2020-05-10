import pytest
from imaplib import IMAP4
from emailclean.domain.email import Email
from emailclean.servers import imap_server
from emailclean.use_cases import imap_use_cases as Imap
from emailclean.requests import request as req
from emailclean.servers.imap_server import ImapClient
from emailclean.servers.imap_server import ImapClient
import threading, sys, localmail_imap, os
from mailbox import mbox
from os import path
from twisted.logger import Logger, textFileLogObserver
from time import sleep

pytestmark = pytest.mark.imap_server

# generator to create temp.mbox files.
NAME_GEN = (f'emailclean_temp_{str(x)}.mbox' for x in range(100, 200))
FILE_LIST = []


# look to see how renotmatic, handles its integeration test setup
# yours just returns a result tupal. but is actuality you probablty
# want a localmail server and imap client running so you can send them
# your requests. The only thing fake will be that the msgs are coming
# from local mail, not googlemail. i  guess, check at which point
# the actual code gets mocked. I think it it esentially only the
# imablib.IMAP4(host=, port=) that will have to be patched in.


@pytest.fixture(scope='function')
def UIDs():
    return [1,2,3,4]

@pytest.fixture(scope='module')
def start_localmail():
    observer = textFileLogObserver(sys.stdout)
    logStdout = Logger(observer=observer)
    # todo: update the file string below. should use abspath and link into set up above
    thread = threading.Thread(
        target=localmail_imap.run,
        args=(2026, 2147, 8881, 'test_inbox.mbox')
)

    thread.start()
    yield

    # revert back to original inbox file
    localmail_imap.imap.INBOX.setFile('test_inbox.mbox')
    # shut down locla imap server
    localmail_imap.shutdown_thread(thread)
    # delete temp mbox files
    [os.remove(x) for x in FILE_LIST]

@pytest.fixture(scope='function')
def set_mailbox():
    # set up mbox file
    mb = mbox('test_inbox.mbox')
    FILE_LIST.append(next(NAME_GEN))
    mb_temp = mbox(FILE_LIST[-1])

    for msgs in mb.items():
        mb_temp.add(msgs[1])
    mb.close()
    mb_temp.close()

    localmail_imap.imap.INBOX.setFile(mb_temp._path)









@pytest.fixture(scope='function')
def imap_client(connection_dict):
    imap_client = ImapClient.connect(connection_dict)
    return imap_client


def test_imap_server_connect(connection_dict, start_localmail):

    imapUC = Imap.ImapConnectUseCase()
    request = req.ImapReqObject.build(conn=connection_dict)
    response = imapUC.execute(request)
    imap_conn = response.value
    assert bool(request) is True
    assert bool(response) is True
    assert isinstance(imap_conn, ImapClient)
    assert imap_conn.connection.noop() == ('OK', [b'NOOP No operation performed'])
    imap_conn.connection.close()

def test_conn_refused_raises_system_error(connection_dict):
    imapUC = Imap.ImapConnectUseCase()
    # set incorrect port
    connection_dict['port'] = 9999
    request = req.ImapReqObject.build(conn=connection_dict)
    response = imapUC.execute(request)
    assert bool(request) is True
    assert bool(response) is False
    assert response.type == 'SystemError'

def test_imap_server_fetch(imap_client):
    imapUC = Imap.ImapFetchUseCase(imap_client)
    request = req.ImapReqObject.build(name="inbox")
    response = imapUC.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    # there are four email in test_inbox.mbox
    assert len(response.value) == 4
    for msg in response.value:
        assert isinstance(msg, type(Email))
    imap_client.connection.close()
    #test sone values here for the returned emails




# test is skipped as methods to update imap server
# from db are required for implementation.
@pytest.mark.skip
def test_imap_server_delete(imap_client, set_mailbox):
    imapUC = Imap.ImapDeleteUseCase(imap_client)
    request = req.ImapReqObject.build(name="inbox")
    response = imapUC.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    assert len(response.value) == 2

def test_imap_mark_as(imap_client, set_mailbox):
#self.imap_client.mark_as(mailbox, flags, UIDs)








"""
result = self.imap_client.new_mb(mailbox)

result = self.imap_client.new_folder(folder)

result = self.imap_client.mark_as(mailbox, flags, UIDs)

result = self.imap_client.move_to(mailbox, UIDs)
"""
