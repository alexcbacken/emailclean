import pytest
import datetime
from emailclean.domain import email as msg


def test_Email_model_init():
    email = msg.Email(uid=1, sender="alex backen <alexcbacken@gmail.com>",
                      date="Sun, 05 Apr 2020 19:28:21 +0000", subject="a test email subject",
                      receiver="email_clean@gmail.com", read=True, flags="")
    assert email.uid == 1
    assert email.sender == "alex backen <alexcbacken@gmail.com>"
    assert email.date == "Sun, 05 Apr 2020 19:28:21 +0000"
    assert email.subject == "a test email subject"
    assert email.receiver == "email_clean@gmail.com"
    assert email.read == True
    assert email.flags == ""


def test_Email_model_from_dict():
    email_dict = {'uid': 1,
                  'sender': "alex backen <alexcbacken@gmail.com>",
                  'date': "Sun, 05 Apr 2020 19:28:21 +0000",
                   'subject': "a test email subject",
                    'receiver': "email_clean@gmail.com",
                  'read': True,
                  'flags': ""}

    email = msg.Email.from_dict(email_dict)
    assert email.uid == 1
    assert email.sender == "alex backen <alexcbacken@gmail.com>"
    assert email.date == "Sun, 05 Apr 2020 19:28:21 +0000"
    assert email.subject == "a test email subject"
    assert email.receiver == "email_clean@gmail.com"
    assert email.read == True



