from fastapi import FastAPI
from pydantic import BaseModel
import requests
import re

from database.models import WordCount, SessionLocal

app = FastAPI()

class WordCountRequest(BaseModel):
    word: str
    url: str

class WordCountResponse(BaseModel):
    count: int

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
    db.refresh(word_count)
    db_count = word_count.count
    db.close()

    # Return response
    return WordCountResponse(count=db_count)
