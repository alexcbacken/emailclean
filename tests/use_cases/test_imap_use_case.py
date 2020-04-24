import pytest
from emailclean.requests import request as req
from emailclean.responses import response as res
from emailclean.use_cases import imap_use_cases as imapUC
from emailclean.domain.email import Email
from unittest import mock,TestCase

#fake results, data return list:
@pytest.fixture()
def uid_list():
    return [20,40,50,60,45,56423]

@pytest.fixture()
def expunge_list():
    return [20,40,50,60,45,56423]

@pytest.fixture()
def msg_list():
    return [
        {"uid":1,
        "sender":"alex backen <alexcbacken@gmail.com>",
        "date":"Sun, 05 Apr 2020 19:28:21 +0000",
        "subject":"a test email subject",
        "receiver":"email_clean@gmail.com",
        "read":True,
         "flags":"//seen"},
        {"uid":"Daily Beast: Scouted <emails@thedailybeast.com>",
         "sender": "Vox Sentences <newsletter@vox.com>",
        "date":"Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        "subject":"Welcome to Scouted!",
        "receiver":"email_clean@gmail.com",
        "read":True,
        "flags":"//seen"},
    {"uid":3,
        "sender":"Morning Brew <crew@morningbrew.com>",
        "date":"Sun, 5 Apr 2020 19:35:51 +0000 (UTC)",
        "subject":"Caution: Morning Brew coming in hot",
        "receiver":"email_clean@gmail.com",
        "read":False,
    "flags":"//seen"},
        {"uid":4,
        "sender":"Vox Sentences <newsletter@vox.com>",
        "date":"Tue, 07 Apr 2020 08:00:38 +1000",
        "subject":"Rotten masks and shared ventilators",
        "receiver":"email_clean@gmail.com",
        "read":True,
        "flags":"//seen"},
        {"uid":5,
        "sender":"Vox Sentences <newsletter@vox.com>",
        "date":"Mon, 06 Apr 2020 19:02:02 -0400",
        "subject":"Trump Removes Watchdog for $2T Virus Bill From Post",
        "receiver":"email_clean@gmail.com",
        "read":False,
        "flags":"//seen"},
        {"uid": 6,
         "sender": "Alex Backen <alexcbacken@gmail.com>",
         "date": "Mon, 06 Apr 2020 15:44:42 +0000 (UTC)",
         "subject": "the times alone are the times alone",
         "receiver": "email_clean@gmail.com",
         "read": False,
         "flags": "//seen"},
        {"uid": 7,
         "sender": "Alex Backen <alexcbacken@gmail.com>",
         "date": "Thu, 06 Apr 2020 15:44:42 +0000 (UTC)",
         "subject": "something for everyone",
         "receiver": "email_clean@gmail.com",
         "read": False,
         "flags": "//seen"}
        ]


def test_Imap_Delete_From_Db_Use_Case(uid_list, expunge_list):
    db = mock.Mock()
    imap_client= mock.Mock()
    db.delete_list.return_value = uid_list
    imap_client.delete.return_value = expunge_list

    Imap_delete_UC = imapUC.ImapDeleteFromDbUseCase(imap_client, db)
    request = req.ImapReqObject.build(type='delete')
    response = Imap_delete_UC.execute(request)
    imap_client.delete.assert_called_with(db.get_delete_list())
    assert bool(request) is True
    assert bool(response) is True
    assert db.get_delete_list.called is True
    assert response.value == [20,40,50,60,45,56423]




def test_Imap_Connect_Use_Case(msg_list):
    db = mock.Mock()
    imap_client= mock.Mock()
    imap_client.connect.return_value = msg_list
    db.get.return_value = 7

    Imap_connect_UC = imapUC.ImapConnectUseCase(imap_client, db)
    request = req.ImapReqObject.build(type='connect')
    response = Imap_connect_UC.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    assert imap_client.connect.called is True
    assert db.write.called is True
    db.get.assert_called_with(type="count")
    assert response.value == 'inbox added to db, db length is 7'

    #

def test_Imap_all_Use_Case(msg_list):
    imap_client= mock.Mock()
    imap_client.all.return_value = msg_list
    Imap_all_UC = imapUC.ImapAllUseCase(imap_client, "INBOX")
    request = req.ImapReqObject.build(type='all')
    response = Imap_all_UC.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    assert imap_client.all.called is True
    assert len(response.value) == 7
    for msg in response.value:
        assert isinstance(msg, type(Email))




