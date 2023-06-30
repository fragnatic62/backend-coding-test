from pydantic import BaseModel


class WordCountBase(BaseModel):
    word: str
    url: str


class WordCountRequest(WordCountBase):
    pass
