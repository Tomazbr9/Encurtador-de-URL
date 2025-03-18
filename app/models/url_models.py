from core.settings import Base
from sqlalchemy import Column, Integer, String, ForeignKey

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False)
    password = Column(String, nullable=False)

class Url(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_url = Column(String, nullable=False)
    long_url = Column(String, nullable=False)
    # user = Column(Integer, ForeignKey('user.id'))
    
