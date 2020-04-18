import pytest


def pytest_addoption(parser):
    parser.addoption("--imap_server", action="store_true", help="run imap-server tests")
    parser.addoption("--postgres", action="store_true", help="run postgres tests")

def pytest_runtest_setup(item):
    if 'imap_server' in item.keywords and not item.config.getvalue("imap_server"):
        pytest.skip("need --imap_server option to run")
    if 'postgres' in item.keywords and not item.config.getvalue("postgres"):
        pytest.skip("need --postgres option to run")
