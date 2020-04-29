import pytest
from emailclean.requests import request as req
from emailclean.domain import email

@pytest.fixture
def msg_list():
    email_2 = email.Email(
        uid=2,
        sender="Daily Beast: Scouted <emails@thedailybeast.com>",
        date="Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        subject="Welcome to Scouted!",
        receiver="email_clean@gmail.com",
        read=True,
        flags=r"/seen")
    email_3 = email.Email(
        uid=2,
        sender="Daily Beast: Scouted <emails@thedailybeast.com>",
        date="Sun, 5 Apr 2020 19:25:56 + 0000(UTC)",
        subject="Welcome to Scouted!",
        receiver="email_clean@gmail.com",
        read=True,
        flags=r"/seen")
    msg_list = [email_3, email_2]
    return msg_list




def test_build_Db_request_no_parameters():
    request = req.DbRequestObject.build()
    assert bool(request.fields) is False
    assert bool(request) is True

def test_build_Db_request_incorrect_parameter_types():
    request = req.DbRequestObject.build(msgs='message')
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == {'parameter': 'msgs', 'problem': "incorrect type try <class 'list'>"}
    assert bool(request) is False


def test_build_Db_request_incorrect_value_types():
    request = req.DbRequestObject.build(msgs='bill', flags="tony")
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == {'parameter': 'flags', 'problem': "incorrect type try <class 'list'>"}
    assert bool(request) is False

def test_build_Db_request_incorrect_args():
    request = req.DbRequestObject.build(tom='bill')
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == {'parameter': 'tom', 'problem': 'incorrect arg value'}
    assert bool(request) is False

def test_build_Db_request_with_parameters(msg_list):
    request = req.DbRequestObject.build(msgs=msg_list, flags=['/seen', '/deleted'])
    assert isinstance(request, req.ValidRequestObject) is True
    assert request.fields.get('msgs') == msg_list
    assert request.fields.get('flags') == ['/seen', '/deleted']
    assert bool(request) is True

def test_build_Db_get_request_no_parameters():
    request = req.DbGetReqObject.build()
    assert bool(request) is False
    assert request.errors == {'parameter': 'kwargs', 'problem': 'none passed'}


def test_build_Db_get_request_incorrect_parameter_types():
    request = req.DbGetReqObject.build(get=["sender"])
    assert bool(request) is False
    assert request.errors == {'parameter': ['sender'], 'problem': 'not an expected argument'}

def test_build_Db_get_request__incorrect_value_types():
    request = req.DbGetReqObject.build(get="push")
    assert bool(request) is False
    assert request.errors == {'parameter': 'push', 'problem': 'not an expected argument'}










