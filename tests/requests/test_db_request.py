import pytest
from emailclean.requests import db_request as req

def test_build_Db_request_no_parameters():
    request = req.DbGetReqObject()
    assert request.type is None
    assert bool(request) is True

def test_build_Db_request_sender_list():
    request = req.DbGetReqObject(type="sender")
    assert request.type == "sender"
    assert bool(request) is True


def test_build_Db_request_delete():
    request = req.DbGetReqObject(type="delete")
    assert request.type == "delete"
    assert bool(request) is True


def test_build_Db_request_count():
    request = req.DbGetReqObject(type="count")
    assert request.type == "count"
    assert bool(request) is True

