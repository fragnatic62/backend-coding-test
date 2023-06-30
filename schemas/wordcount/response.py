from pydantic import BaseModel
from typing import List

from schemas.wordcount.request import WordCountBase


class WordCountResponse(WordCountBase):
    id: int
    count: int


class WordCountDBResponse(BaseModel):
    word_counts: List[WordCountResponse]
