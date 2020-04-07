import pytest
import json

from emailclean.serialisers import email_json_serialiser as ser
from emailclean.domain import message as msg



def test_serialise_domain_email():
    email = msg.Email(uid=1, sender="alex backen <alexcbacken@gmail.com>",
                      date="Sun, 05 Apr 2020 19:28:21 +0000", subject="a test email subject",
                      receiver="email_clean@gmail.com")

    expected_json = """
            {
            "uid": "1",
            "sender": "alex backen <alexcbacken@gmail.com>",
            "date": "Sun, 05 Apr 2020 19:28:21 +0000",
            "subject": "a test email subject",
            "receiver": "email_clean@gmail.com"
            }
        """

    # actual json string. serialised using our own serialiser
    # ser.RoomJsonEncoder.
    json_email = json.dumps(email, cls=ser.EmailJsonEncoder)
    print(json_email)
    print(expected_json)
    assert json.loads(json_email) == json.loads(expected_json)
