import pytest
from emailclean.requests import request as req


def test_build_Imap_request_no_parameters():
    request = req.ImapReqObject.build()
    assert request.has_errors() is True
    assert request.errors == {'parameter': 'kwargs', 'problem': 'none passed'}
    assert bool(request) is False

def test_build_Imap_request_With_Incorrect_Value_types():
    request = req.ImapReqObject.build(name=[], UIDs="big")
    assert request.has_errors() is True
    assert request.errors == {'parameter': 'UIDs', 'problem': "incorrect type try <class 'list'>"}
    assert bool(request) is False

def test_build_Imap_request_With_parameters():
    request = req.ImapReqObject.build(UIDs=[1,2,3],name="mailbox")
    assert request.fields == {'name': 'mailbox',
                              'UIDs':[1,2,3]}
    assert bool(request) is True












