import pytest

@pytest.fixture(scope='session')
def response_value():
    return {'key': ['value1', 'value2']}


@pytest.fixture(scope='session')
def response_type():
    return 'ResponseError'


@pytest.fixture(scope='session')
def response_message(scope='session'):
    return 'This is a response error'
