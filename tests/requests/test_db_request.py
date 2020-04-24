import pytest
from emailclean.requests import request as req


def test_build_Imap_request_no_parameters():
    request = req.DbGetReqObject.build()
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == [{'message': "type not specified try: ['sender', 'count', 'delete']",
                               'parameter': 'type'}]
    assert bool(request) is False

def test_build_Imap_request_incorrect_parameters():
    request = req.DbGetReqObject.build(type='incorrect')
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == [{'message': "type=incorrect is invalid. try: ['sender', 'count', 'delete']",
                               'parameter': 'type'}]
    assert bool(request) is False

def test_build_Db_request_sender_list():
    request = req.DbGetReqObject.build(type="sender")
    assert request.type == "sender"
    assert bool(request) is True


def test_build_Db_request_delete():
    request = req.DbGetReqObject.build(type="delete")
    assert request.type == "delete"
    assert bool(request) is True


def test_build_Db_request_count():
    request = req.DbGetReqObject.build(type="count")
    assert request.type == "count"
    assert bool(request) is True

