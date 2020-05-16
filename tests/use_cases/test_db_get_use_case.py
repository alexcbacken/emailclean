import pytest
from emailclean.use_cases import db_get_use_case as db_uc
from emailclean.requests import request as req
from emailclean.domain import email
from emailclean.requests import request
from unittest import mock

#fixture below is unneeded, but kept incase useful for future tests.


@pytest.fixture
def msg_list():
    email_1 = email.Email(
        uid=1,
        sender="alex backen <alexcbacken@gmail.com>",
        date="Sun, 05 Apr 2020 19:28:21 +0000",
        subject="a test email subject",
        receiver="email_clean@gmail.com",
        read=True,
        flags=r"/seen")

    email_2 = email.Email(
        uid=2,
        sender="Daily Beast: Scouted <emails@thedailybeast.com>",
        date="Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        subject="Welcome to Scouted!",
        receiver="email_clean@gmail.com",
        read=True,
        flags=r"/seen")

    email_3 = email.Email(
        uid=3,
        sender="Morning Brew <crew@morningbrew.com>",
        date="Sun, 5 Apr 2020 19:35:51 +0000 (UTC)",
        subject="Caution: Morning Brew coming in hot",
        receiver="email_clean@gmail.com",
        read=False,
        flags=r"/seen")

    email_4 = email.Email(
        uid=4,
        sender="Vox Sentences <newsletter@vox.com>",
        date="Tue, 07 Apr 2020 08:00:38 +1000",
        subject="Rotten masks and shared ventilators",
        receiver="email_clean@gmail.com",
        read=True,
        flags=r"/answered")

    email_5 = email.Email(
        uid=5,
        sender="Vox Sentences <newsletter@vox.com>",
        date="Mon, 06 Apr 2020 19:02:02 -0400",
        subject="Trump Removes Watchdog for $2T Virus Bill From Post",
        receiver="email_clean@gmail.com",
        read=False,
        flags="")

    email_6 = email.Email(
        uid=6,
        sender="Alex Backen <alexcbacken@gmail.com>",
        date="Mon, 06 Apr 2020 15:44:42 +0000 (UTC)",
        subject="the times alone are the times alone",
        receiver="email_clean@gmail.com",
        read=True,
        flags="")

    email_6 = email.Email(
        uid=7,
        sender="Alex Backen <alexcbacken@gmail.com>",
        date="Thu, 06 Apr 2020 15:44:42 +0000 (UTC)",
        subject="something for everyone",
        receiver="email_clean@gmail.com",
        read=True,
        flags="")
    return [email_1,email_2,email_3,email_4,email_5,email_6]


@pytest.fixture
def sender_list():
    s_list = [
        {"sender": "Alex Backen <alexcbacken@gmail.com>",
            "no": 100, "frequency": "daily",
         "first": "Apr 2000", "last": "Jan 2020"},
        {"sender": "Vox Sentences <newsletter@vox.com>",
            "no": 500, "frequency": "monthly",
         "first": "Apr 2000", "last": "Apr 2020"},
        {"sender": "Morning Brew <crew@morningbrew.com>",
            "no": 347, "frequency": "weekly",
         "first": "Sep 2011", "last": "Apr 2019"},
        {"sender": "Daily Beast: Scouted <emails@thedailybeast.com>",
            "no": 146, "frequency": "< monthly",
         "first": "Jan 2018", "last": "Feb 2020"},
        {"sender": "The New York Times <nytdirect@nytimes.com>",
            "no": 210, "frequency": "daily",
         "first": "Apr 2016", "last": "Apr 2019"},
            ]

@pytest.fixture
def delete_list():
    d_list = [
        {"sender": "Alex Backen <alexcbacken@gmail.com>",
            "no": 100},
        {"sender": "Vox Sentences <newsletter@vox.com>",
            "no": 500},
        {"sender": "Morning Brew <crew@morningbrew.com>",
            "no": 347},
        {"sender": "Daily Beast: Scouted <emails@thedailybeast.com>",
            "no": 146},
        {"sender": "The New York Times <nytdirect@nytimes.com>",
            "no": 210,}
            ]
@pytest.fixture
def count():
    count = [1356,]

@pytest.fixture
def UIDs():
    return [1,3,5,6,]

@pytest.fixture
def flags():
    return ['/seen', '/deleted']

def test_Db_create_use_case(msg_list):
    db = mock.Mock()
    db.create.return_value = "ok"
    name="inbox"
    db_create_use_case = db_uc.DbCreateUseCase(db)
    request = req.DbRequestObject.build(name=name, msgs=msg_list)
    response = db_create_use_case.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    db.create.assert_called_with(msg_list, name)
    assert response.value == "ok"

def test_Db_mark_as_use_case(UIDs, flags):
    db = mock.Mock()
    db.mark_as.return_value = "ok"
    db_mark_as_use_case = db_uc.DbMarkAsUseCase(db)
    request = req.DbRequestObject.build(UIDs=UIDs,flags=flags)
    response = db_mark_as_use_case.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    db.mark_as.assert_called_with(UIDs, flags)
    assert response.value == "ok"

def test_Db_get_use_case(sender_list):
    db = mock.Mock()
    db.get.return_value = sender_list
    db_get_use_case = db_uc.DbGetUseCase(db)
    request = req.DbGetReqObject.build(get='sender')
    response = db_get_use_case.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    db.get.assert_called_with(get='sender')
    assert response.value == sender_list

def test_Db_delete_db_use_case():
    db = mock.Mock()
    db.delete.return_value = "ok"
    db_delete_use_case = db_uc.DbDeleteDbUseCase(db)
    request = req.DbRequestObject.build()
    response = db_delete_use_case.execute(request)
    assert bool(request) is True
    assert bool(response) is True
    assert db.delete.called is True
    assert response.value == "ok"







