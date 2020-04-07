import pytest
from emailclean.requests import email_list_request as req

def test_build_Db_request_no_parameters():
    request = req.DbReqObject()
    assert request.type is None
    assert bool(request) is True

def test_build_Db_request_sender_list():
    request = req.DbReqObject(type="sender")
    assert request.type == "sender"
    assert bool(request) is True


def test_build_Db_request_delete():
    request = req.DbReqObject(type="delete")
    assert request.type == "delete"
    assert bool(request) is True


def test_build_Db_request_count():
    request = req.DbReqObject(type="count")
    assert request.type == "count"
    assert bool(request) is True

