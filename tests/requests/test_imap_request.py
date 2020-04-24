import pytest
from emailclean.requests import request as req


def test_build_Imap_request_no_parameters():
    request = req.ImapReqObject.build()
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == [{'parameter': 'type',
                               'message': "type not specified try: ['delete', 'all', 'connect']"}]
    assert bool(request) is False

def test_build_Imap_request_incorrect_parameters():
    request = req.ImapReqObject.build(type='incorrect')
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == [{'message': "type=incorrect is invalid. try: ['delete', 'all', 'connect']",
                               'parameter': 'type'}]
    assert bool(request) is False


def test_build_Imap_request_connect():
    request = req.ImapReqObject.build(type="connect")
    assert request.type == "connect"
    assert bool(request) is True


def test_build_Imap_request_delete():
    request = req.ImapReqObject.build(type="delete")
    assert request.type == "delete"
    assert bool(request) is True

def test_build_Imap_request_all():
    request = req.ImapReqObject.build(type="all")
    assert request.type == "all"
    assert bool(request) is True






