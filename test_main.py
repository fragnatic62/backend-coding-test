import pytest
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)

def test_word_count():
    request_data = {
        'word': 'fit',
        'url': 'https://www.virtusize.jp/'
    }

    response = client.post('/wordcount', json=request_data)
    assert response.status_code == 200
    assert response.json() == {'count':6}