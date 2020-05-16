from emailclean.database.SQLite_objects import email

def test_db_populates(SQLite_session):
    assert SQLite_session.query(email).count() == 7

