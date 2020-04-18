import pytest

@pytest.fixture(scope='session')
def imap_conection:
    with imaplib.IMAP4_SSL(host='imap.gmail.com', port=993) as M:
        M.login('emailclean321@gmail.com', "mail_clean345")
        M.select()




