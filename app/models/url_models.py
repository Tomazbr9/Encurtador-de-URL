from app.core.settings import Base
from sqlalchemy import Column, Integer, String

class OriginalUrl(Base):
    __tablename__ = 'original_url'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    original_url = Column(String, nullable=False)

class ShortUrl(Base):
    __tablename__ = 'short_url'

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_original = Column(String, nullable=False)
    
