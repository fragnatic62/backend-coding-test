import os

def pytest_configure():
    os.environ['MY_FLAG'] = 'True'
    os.environ['DB_CONNECTION_STRING'] = 'sqlite:///test_wordcount.db'
