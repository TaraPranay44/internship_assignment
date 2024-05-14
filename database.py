# database.py

from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URI = 'sqlite:///logs.db'
Base = declarative_base()

def get_engine():
    return create_engine(DATABASE_URI)

def get_session():
    engine = get_engine()
    Session = sessionmaker(bind=engine)
    return Session()

class LogEntry(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True)
    level = Column(String)
    log_string = Column(String)
    timestamp = Column(DateTime)
    source = Column(String)

def setup_database():
    engine = get_engine()
    Base.metadata.create_all(engine)
