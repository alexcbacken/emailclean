import pytest
from emailclean.database.SQLite_objects import email
from emailclean.database.SQLite_database import SqlliteSessionMaker
from sqlalchemy import text

@pytest.fixture(scope='function')
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

def test_db_create(inbox_email_list, session):
    assert session.is_active == True
    # given a list of email objects and a inbox name, create table
    result = session.create(inbox_email_list)
    assert session.query(email).count() == 7
    assert session.query(email).filter(email.mailbox == 'inbox').count() == 7
    assert result == "Success"

def test_multiple_mailbox_create(inbox_email_list, mybox_email_list, session):
    assert session.query(email).count() == 0
    session.create(mybox_email_list)
    session.create(inbox_email_list)
    query = session.query(email)
    assert query.filter(text('emails.mailbox = "mybox"')).count() == 7
    assert query.filter(text('emails.mailbox = "inbox"')).count() == 7
    assert query.filter(email.mailbox == 'inbox').count() == 7
    assert query.filter(email.mailbox == 'mybox').count() == 7
    assert query.filter_by(mailbox='inbox').count() == 7
    assert query.filter_by(mailbox='mybox').count() == 7

"""
class DbCreateUseCase:
            email_list = request.fields.get('msgs')
            name = request.fields.get('name')
            result = self.db.create(email_list, name)
class DbMarkAsUseCase:
            UIDs = request.fields.get('UIDs')
            flags = request.fields.get('flags')
            result = self.db.mark_as(UIDs, flags)
class DbGetUseCase:
            get_type = request.fields.get('get')
            result = self.db.get(get=get_type)
class DbDeleteDbUseCase:
            result = self.db.delete()
"""
