import os
from dotenv import load_dotenv
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker,declarative_base

load_dotenv()

connection_string = os.getenv('DB_CONNECTION_STRING')
engine = create_engine(connection_string)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

class WordCount(Base):
    __tablename__ = 'word_counts'

    id = Column(Integer, primary_key=True)
    word = Column(String)
    url = Column(String)
    count = Column(Integer)

Base.metadata.create_all(bind=engine)


# 'sqlite:///wordcount.db'