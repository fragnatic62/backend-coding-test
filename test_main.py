import pytest
import json
import requests_mock
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_word_count():
    """
    This API should be working 🎇🎆✨
    """
    
    request_data = {
        'word': 'fit',
        'url': 'https://www.virtusize.jp/'
    }

    response = client.post('/wordcount', json=request_data)
    assert response.status_code == 200
    response_json = response.json()
    assert response_json['word'] == 'fit'
    assert response_json['url'] == 'https://www.virtusize.jp/'
    assert response_json['count'] == 13

# def test_word_count_exact_occurrence():
#     """
#     Should return the exact number of word occurrence without case sensitivity
#     """
#     url = 'https://www.virtusize.jp/'
#     expected_count = 3
#     request_data = {
#         'word': 'fit',
#         'url': url
#     }

#     with requests_mock.Mocker() as m:
#         # Stub the requests.get call with a mocked response
#         m.get(url, text='<html>fit fit Fit</html>')

#         response = client.post('/wordcount', json=request_data)

#     assert response.status_code == 200
#     import pdb; pdb.set_trace()
#     assert response.json() == {'count': expected_count}


# def test_word_count_no_fitting():
#     """
#     Should not count fitting as part of the word fit
#     """
#     url = 'https://www.virtusize.jp/'
#     expected_count = 3
#     request_data = {
#         'word': 'fit',
#         'url': url
#     }

#     with requests_mock.Mocker() as m:
#         # Stub the requests.get call with a mocked response
#         m.get(url, text='<html>fit fit Fit fitting</html>')

#         response = client.post('/wordcount', json=request_data)

#     assert response.status_code == 200
#     assert response.json() == {'count': expected_count}


# def test_word_count_word_not_found():
#     """
#     Should return 0 when the word is not found
#     """
#     url = 'https://www.virtusize.jp/'
#     expected_count = 0
#     request_data = {
#         'word': 'test',
#         'url': url
#     }

#     with requests_mock.Mocker() as m:
#         # Stub the requests.get call with a mocked response
#         m.get(url, text='<html>fit fit Fit fitting</html>')

#         response = client.post('/wordcount', json=request_data)

#     assert response.status_code == 200
#     assert response.json() == {'count': expected_count}


# def test_word_count_special_characters():
#     """
#     Should work with special characters in the word
#     """
#     url = 'https://www.virtusize.jp/'
#     expected_count = 1
#     request_data = {
#         'word': 'f!t',
#         'url': url
#     }

#     with requests_mock.Mocker() as m:
#         # Stub the requests.get call with a mocked response
#         m.get(url, text='<html>fit fit F!t fitting</html>')

#         response = client.post('/wordcount', json=request_data)

#     assert response.status_code == 200
#     assert response.json() == {'count': expected_count}


# def test_word_count_with_punctuation():
#     """
#     Should return the exact number of word occurrences without case sensitivity,
#     considering 'fit' with a comma or period after it
#     """
#     url = 'https://www.virtusize.jp/'
#     expected_count = 3
#     request_data = {
#         'word': 'fit',
#         'url': 'https://www.virtusize.jp/'
#     }

#     with requests_mock.Mocker() as m:
#         # Stub the requests.get call with a mocked response
#         m.get(url, text='<html>fit, fit Fit. fitting -fit-</html>')

#         with TestClient(app) as client:
#             response = client.post('/wordcount', json=request_data)
#             assert response.status_code == 200
#             assert response.json() == {'count': expected_count}