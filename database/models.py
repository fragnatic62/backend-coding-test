from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///wordcount.db')
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class WordCount(Base):
    __tablename__ = 'word_counts'

    id = Column(Integer, primary_key=True)
    word = Column(String)
    url = Column(String)
    count = Column(Integer)

Base.metadata.create_all(bind=engine)