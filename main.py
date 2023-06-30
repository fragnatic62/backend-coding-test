from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import re

from database.models import WordCount, SessionLocal
from schemas.wordcount.request import WordCountRequest
from schemas.wordcount.response import WordCountDBResponse, WordCountResponse

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post('/wordcount', response_model=WordCountResponse)
async def word_count(request_data: WordCountRequest) -> WordCountResponse:
    # Retrieve the word and webpage URL from the request
    text_search = request_data.word
    url = request_data.url

    # Send GET request to get the webpage source
    response = requests.get(url)
    html_source = response.text

    # Splitting HTML source into individual word and occurrence
    count = len(re.findall(r'(?<!-)\b{}\b(?<!-)' .format(re.escape(text_search.lower())), html_source.lower()))

    # Save to DB
    db = SessionLocal()
    word_count = WordCount(word=text_search, url=url, count=count)
    db.add(word_count)
    db.commit()

    # Access the ID after the record is committed
    db.refresh(word_count)
    db_id = word_count.id
    db_count = word_count.count

    db.close()

    # Return response
    return WordCountResponse(id=db_id, word=text_search, url=url, count=db_count)


@app.get('/wordcounts', response_model=WordCountDBResponse)
async def get_word_counts() -> WordCountDBResponse:
    db = SessionLocal()
    word_counts = db.query(WordCount).all()
    db.close()

    word_counts_response = [
        WordCountResponse(id=word_count.id, word=word_count.word, url=word_count.url, count=word_count.count) for word_count in word_counts
    ]
    return WordCountDBResponse(word_counts=word_counts_response)
