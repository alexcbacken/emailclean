import pytest
import datetime
from emailclean.domain import message as msg

pytestmark = pytest.mark.unit

def test_Email_model_init():
    email = msg.Email(uid=1, sender="alex backen <alexcbacken@gmail.com>",
                      date=datetime.date(2020, 1, 23), subject="a test email subject",
                      receiver="email_clean@gmail.com")
    assert email.uid == 1
    assert email.sender == "alex backen <alexcbacken@gmail.com>"
    assert email.date == datetime.date(2020, 1, 23)
    assert email.subject == "a test email subject"
    assert email.receiver == "email_clean@gmail.com"

def test_Email_model_from_dict():
    email_dict = {'uid': 1,
                  'sender': "alex backen <alexcbacken@gmail.com>",
                  'date': datetime.date(2020, 1, 23),
                   'subject': "a test email subject",
                    'receiver': "email_clean@gmail.com"}

    email = msg.Email.from_dict(email_dict)
    assert email.uid == 1
    assert email.sender == "alex backen <alexcbacken@gmail.com>"
    assert email.date == datetime.date(2020, 1, 23)
    assert email.subject == "a test email subject"
    assert email.receiver == "email_clean@gmail.com"

def test_Email_model_init_with_date_string():
    email = msg.Email(uid=1, sender="alex backen <alexcbacken@gmail.com>",
                      date="Thu, 23 Jan 2020 06:10:04 -0400 (EDT)", subject="a test email subject",
                      receiver="email_clean@gmail.com")
    assert email.uid == 1
    assert email.sender == "alex backen <alexcbacken@gmail.com>"
    assert email.date == datetime.date(2020, 1, 23)
    assert email.subject == "a test email subject"
    assert email.receiver == "email_clean@gmail.com"


