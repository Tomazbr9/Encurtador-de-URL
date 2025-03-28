from core.settings import Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class UserModel(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)

    urls = relationship('UrlModel', back_populates="user")

    def __repr__(self):
        return f'User [Username={self.username}, Password={self.password}]'

class UrlModel(Base):
    __tablename__ = 'url'

    id = Column(Integer, primary_key=True, autoincrement=True)
    short_url = Column(String, nullable=False)
    long_url = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=True)

    user = relationship('UserModel', back_populates="urls")

    def __repr__(self):
        return f'URL [Short Url={self.short_url}, Long Url={self.long_url}]'
    
