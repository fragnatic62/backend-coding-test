from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

from main import app
from database.models import engine
from database.models import WordCount
from schemas.wordcount.response import WordCountDBResponse, WordCountResponse


client = TestClient(app)


def test_get_word_counts():
    # Prepare test data
    with Session(engine) as session:
        # Create some sample WordCount records
        word_count_1 = WordCount(word='fit', url='https://www.example.com', count=10)
        word_count_2 = WordCount(word='test', url='https://www.example.com', count=5)
        session.add_all([word_count_1, word_count_2])
        session.commit()

        # Eagerly load the required attributes
        word_counts = session.query(WordCount.id, WordCount.word, WordCount.url, WordCount.count).all()

    # Perform the API request
    response = client.get('/wordcounts')

    # Check the response status code
    assert response.status_code == 200

    # Check the response model
    response_data = response.json()
    response_data = WordCountDBResponse(**response_data)
    assert isinstance(response_data, WordCountDBResponse)
    assert isinstance(response_data.word_counts, list)
    assert all(isinstance(word_count, WordCountResponse) for word_count in response_data.word_counts)

    # Check the returned word count data
    expected_word_counts = [
        WordCountResponse(
            id=word_count.id,
            word=word_count.word,
            url=word_count.url,
            count=word_count.count
        )
        for word_count in word_counts
    ]
    assert response_data.word_counts == expected_word_counts
