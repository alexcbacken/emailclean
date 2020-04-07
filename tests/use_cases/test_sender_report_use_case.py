import pytest
from emailclean.use_cases import sender_list_use_case as sl
from emailclean.domain import email as msg
from emailclean.requests import db_request
from unittest import mock

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

def test_sender_list_use_case(domain_email):
    repo = mock.Mock()
    repo.get.return_value =domain_email

    sender_list_use_case = sl.SenderListUseCase(repo)
    request = db_request.DbReqObject()
    response = sender_list_use_case.execute(request)




