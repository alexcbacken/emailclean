import pytest
from emailclean.requests import request as req


def test_build_Db_request_no_parameters():
    request = req.DbGetReqObject.build()
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == [{'message': "invalid args: []  try: ['type=']", 'parameter': 'invalid args'}]
    assert bool(request) is False

def test_build_Db_request_incorrect_parameters():
    request = req.DbGetReqObject.build(type='incorrect')
    assert isinstance(request, req.InvalidRequestObject) is True
    assert request.errors == [{'message': "invalid args: ['type=incorrect']  try: ['type=']",
  'parameter': 'invalid args'}]
    assert bool(request) is False

def test_build_Db_request_sender_list():
    request = req.DbGetReqObject.build(type="sender")
    assert request.fields == {'type':"sender"}
    assert bool(request) is True


def test_build_Db_request_delete():
    request = req.DbGetReqObject.build(type="delete")
    assert request.fields == {'type':"delete"}
    assert bool(request) is True

def test_build_Db_request_all():
    request = req.DbGetReqObject.build(type="all")
    assert request.fields == {'type':"all"}
    assert bool(request) is True




