import pytest
from emailclean.use_cases import db_get_use_case as db_lst

from emailclean.requests import db_request
from unittest import mock

#fixture below is unneeded, but kept incase useful for future tests.

"""
@pytest.fixture
def domain_email():
    email_1 = msg.Email(
        uid=1,
        sender="alex backen <alexcbacken@gmail.com>",
        date="Sun, 05 Apr 2020 19:28:21 +0000",
        subject="a test email subject",
        receiver="email_clean@gmail.com",
        read=True)

    email_2 = msg.Email(
        uid=2,
        sender="Daily Beast: Scouted <emails@thedailybeast.com>",
        date="Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        subject="Welcome to Scouted!",
        receiver="email_clean@gmail.com",
        read=True)

    email_3 = msg.Email(
        uid=3,
        sender="Morning Brew <crew@morningbrew.com>",
        date="Sun, 5 Apr 2020 19:35:51 +0000 (UTC)",
        subject="Caution: Morning Brew coming in hot",
        receiver="email_clean@gmail.com",
        read=False)

    email_4 = msg.Email(
        uid=4,
        sender="Vox Sentences <newsletter@vox.com>",
        date="Tue, 07 Apr 2020 08:00:38 +1000",
        subject="Rotten masks and shared ventilators",
        receiver="email_clean@gmail.com",
        read=True)

    email_5 = msg.Email(
        uid=5,
        sender="Vox Sentences <newsletter@vox.com>",
        date="Mon, 06 Apr 2020 19:02:02 -0400",
        subject="Trump Removes Watchdog for $2T Virus Bill From Post",
        receiver="email_clean@gmail.com",
        read=False)

    email_6 = msg.Email(
        uid=6,
        sender="Alex Backen <alexcbacken@gmail.com>",
        date="Mon, 06 Apr 2020 15:44:42 +0000 (UTC)",
        subject="the times alone are the times alone",
        receiver="email_clean@gmail.com",
        read=True)

    email_6 = msg.Email(
        uid=7,
        sender="Alex Backen <alexcbacken@gmail.com>",
        date="Thu, 06 Apr 2020 15:44:42 +0000 (UTC)",
        subject="something for everyone",
        receiver="email_clean@gmail.com",
        read=True)
"""

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

def test_sender_list_use_case(sender_list):
    repo = mock.Mock()
    repo.get.return_value =sender_list

    sender_list_use_case = db_lst.SenderListUseCase(repo)
    request = db_request.DbGetReqObject(type="sender")
    response = sender_list_use_case.execute(request)

    assert bool(request) is True
    assert bool(response) is True
    repo.get.assert_called_with(type="sender")
    assert response.value == sender_list

def test_delete_list_use_case(delete_list):
    repo = mock.Mock()
    repo.get.return_value =delete_list

    deleted_list_use_case = db_lst.DeleteListUseCase(repo)
    request = db_request.DbGetReqObject(type="delete")
    response = deleted_list_use_case.execute(request)

    assert bool(request) is True
    assert bool(response) is True
    repo.get.assert_called_with(type="delete")
    assert response.value == delete_list

def test_count_use_case(count):
    repo = mock.Mock()
    repo.get.return_value =count

    count_use_case = db_lst.CountUseCase(repo)
    request = db_request.DbGetReqObject(type="count")
    response = count_use_case.execute(request)

    assert bool(request) is True
    assert bool(response) is True
    repo.get.assert_called_with(type="count")
    assert response.value == count



