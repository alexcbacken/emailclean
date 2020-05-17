import pytest
from emailclean.database.SQLite_objects import email
from emailclean.database.SQLite_database import SqlliteSessionMaker



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



def test_db_create(SQLite_data, session):
    print(session.get_bind())
    assert session.is_active == True
    name = "inbox"
    # given a list of email objects and a inbox name, create table
    result = session.create(SQLite_data, name)
    assert session.query(email).count() == 7
    assert result == "Success"





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
