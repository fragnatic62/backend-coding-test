from fastapi import FastAPI
from pydantic import BaseModel
import requests

app = FastAPI()

class WordCountRequest(BaseModel):
    word: str
    url: str

class WordCountResponse(BaseModel):
    count: int

@app.post('/wordcount',response_model=WordCountResponse)
async def word_count(request_data: WordCountRequest) -> WordCountResponse:
    # Retrived the word and webpage URL from request
    text_search = request_data.word
    url = request_data.url

    # Send GET request to get the webpage source
    response = requests.get(url)
    html_source = response.text

    # Splitting HTML source into individual word and occurence
    count = sum(1 for word in html_source.split() if word.lower() == text_search.lower())

    # Save to DB(Optional)

    # Return response
    return WordCountResponse(count=count)