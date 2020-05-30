import pytest
from emailclean.database.SQLite_objects import email
from emailclean.database.SQLite_database import SqlliteSessionMaker
from sqlalchemy import text

@pytest.fixture(scope='session')
def session():
    """
    for each test function, create a new session maker, session and therefore, engine. at the end of each function,
    delete the session and engine
    :return:
    """
    session_maker = SqlliteSessionMaker()
    session = session_maker()
    yield session
    session.close()
    session.get_bind().dispose()

@pytest.fixture(scope='function')
def populated_session(session, inbox_email_list):
    session.create(inbox_email_list)
    yield session
    session.query(email).delete()
    session.commit()

@pytest.fixture(scope='function')
def unpopulated_session(session):
    yield session
    session.query(email).delete()
    session.commit()

def test_db_create(inbox_email_list, unpopulated_session):
    assert unpopulated_session.is_active == True
    # given a list of email objects and a inbox name, create table
    result = unpopulated_session.create(inbox_email_list)
    assert unpopulated_session.query(email).count() == 7
    assert unpopulated_session.query(email).filter(email.mailbox == 'inbox').count() == 7
    assert result == "Success"


def test_db_multiple_mailbox_create(inbox_email_list, mybox_email_list, unpopulated_session):
    assert unpopulated_session.query(email).count() == 0
    unpopulated_session.create(mybox_email_list)
    unpopulated_session.create(inbox_email_list)
    query = unpopulated_session.query(email)
    assert query.filter(text('emails.mailbox = "mybox"')).count() == 7
    assert query.filter(text('emails.mailbox = "inbox"')).count() == 7
    assert query.filter(email.mailbox == 'inbox').count() == 7
    assert query.filter(email.mailbox == 'mybox').count() == 7
    assert query.filter_by(mailbox='inbox').count() == 7
    assert query.filter_by(mailbox='mybox').count() == 7

def test_db_mark_as(inbox_email_list, populated_session, flags):
    uids = [dic['uid'] for dic in inbox_email_list]
    name = 'inbox'
    result = populated_session.mark_as(uids, name, flags)
    assert result == 7


def test_db_get_by_sender(populated_session):
    result = populated_session.get(get="by_sender")
    assert result == {'inbox': [(1, 'alex backen <alexcbacken@gmail.com>'),
                                (3, 'Vox Sentences <newsletter@vox.com>'),
                                (1, 'Morning Brew <crew@morningbrew.com>'),
                                (2, 'Alex Backen <alexcbacken@gmail.com>')]}



def test_db_get_all(populated_session):
    result = populated_session.get(get="all")
    assert len(result['inbox']) == 7
    for x in result['inbox']:
        assert isinstance(x, email)

def test_db_get_deleted(populated_session):
    result = populated_session.get(get="deleted")
    assert isinstance(result, dict) == True





"""
class DbGetUseCase:
            get_type = request.fields.get('get')
            result = self.db.get(get=get_type)

class DbDeleteDbUseCase:
            result = self.db.delete()
"""
