import requests_mock
from fastapi.testclient import TestClient
import os
from dotenv import load_dotenv
from database.models import SessionLocal
from main import app

client = TestClient(app)

def validate_test_database_from_sessionlocal():
    session = SessionLocal()
    assert session.bind.url == 'sqlite:///test_wordcount.db'

def validate_environment_variable():
    load_dotenv()  # Load environment variables from .env file
    my_flag_str = os.getenv('MY_FLAG')
    my_flag = my_flag_str.lower() in ['true', '1', 'yes', 'y']
    assert my_flag is True


def test_word_count_e2e():
    """
    This API should be working 🎇🎆✨
    """
    
    request_data = {
        'word': 'fit',
        'url': 'https://www.virtusize.jp/'
    }

    response = client.post('/wordcount', json=request_data)
    assert response.status_code == 200
    expected_response = {'word': 'fit', 'url': 'https://www.virtusize.jp/', 'count': 13}
    assert all(item in response.json().items() for item in expected_response.items())

def test_word_count_exact_occurrence_e2e():
    """
    Should return the exact number of word occurrence without case sensitivity
    """
    url = 'https://www.virtusize.jp/'
    request_data = {
        'word': 'fit',
        'url': url
    }

    with requests_mock.Mocker() as m:
        # Stub the requests.get call with a mocked response
        m.get(url, text='<html>fit fit Fit</html>')

        response = client.post('/wordcount', json=request_data)
        expected_response = {'count': 3}
        assert response.status_code == 200
        assert all(item in response.json().items() for item in expected_response.items())


def test_word_count_no_fitting_e2e():
    """
    Should not count fitting as part of the word fit
    """
    url = 'https://www.virtusize.jp/'
    request_data = {
        'word': 'fit',
        'url': url
    }

    with requests_mock.Mocker() as m:
        # Stub the requests.get call with a mocked response
        m.get(url, text='<html>fit fit Fit fitting</html>')

        response = client.post('/wordcount', json=request_data)

        expected_response = {'count': 3}
        assert response.status_code == 200
        assert all(item in response.json().items() for item in expected_response.items())


def test_word_count_word_not_found_e2e():
    """
    Should return 0 when the word is not found
    """
    url = 'https://www.virtusize.jp/'
    request_data = {
        'word': 'test',
        'url': url
    }

    with requests_mock.Mocker() as m:
        # Stub the requests.get call with a mocked response
        m.get(url, text='<html>fit fit Fit fitting</html>')

        response = client.post('/wordcount', json=request_data)

        expected_response = {'count': 0}
        assert response.status_code == 200
        assert all(item in response.json().items() for item in expected_response.items())


def test_word_count_special_characters_e2e():
    """
    Should work with special characters in the word
    """
    url = 'https://www.virtusize.jp/'
    request_data = {
        'word': 'f!t',
        'url': url
    }

    with requests_mock.Mocker() as m:
        # Stub the requests.get call with a mocked response
        m.get(url, text='<html>fit fit F!t fitting</html>')

        response = client.post('/wordcount', json=request_data)

        expected_response = {'count': 1}
        assert response.status_code == 200
        assert all(item in response.json().items() for item in expected_response.items())


def test_word_count_with_punctuation_e2e():
    """
    Should return the exact number of word occurrences without case sensitivity,
    considering 'fit' with a comma or period after it
    """
    url = 'https://www.virtusize.jp/'
    expected_count = 3
    request_data = {
        'word': 'fit',
        'url': 'https://www.virtusize.jp/'
    }

    with requests_mock.Mocker() as m:
        # Stub the requests.get call with a mocked response
        m.get(url, text='<html>fit, fit Fit. fitting -fit-</html>')

        with TestClient(app) as client:
            response = client.post('/wordcount', json=request_data)
            expected_response = {'count': 3}
            assert response.status_code == 200
            assert all(item in response.json().items() for item in expected_response.items())