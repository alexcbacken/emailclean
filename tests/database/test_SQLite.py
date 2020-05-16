import pytest
from emailclean.database.SQLite_objects import email
from emailclean.database.SQLite_database import SqlliteSessionMaker
from sqlalchemy import MetaData



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






# test_session_initialisation



def test_db_create(msg_list, session):
    assert session.is_active == True
    name = "inbox"
    # given a list of email objects and a inbox name, create table
    result = session.create(msg_list, name)
    assert name in session.get_bind().table_names()
    assert result == "Success"

def test_multiple_mailbox_create(msg_list, session):
    #this should now just add the second mailbox to this same database. there
    # is now a column for mailbox
    name = "inbox"
    # given a list of email objects and a inbox name, create table
    result = session.create(msg_list, name)
    name2 = "mybox"
    # given a list of email objects and a inbox name, create table
    result = session.create(msg_list, name2)
    # run a test for the no of records and the value of the mailbox column







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
