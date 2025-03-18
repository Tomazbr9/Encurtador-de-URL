from sqlalchemy import create_engine, Engine
from sqlalchemy.orm import sessionmaker, Session
from .settings import DB_URL
from typing import Optional

class DBConnectionHandler:

    def __init__(self) -> None:
        self.__connection_url: str = DB_URL
        self.__engine: Engine = self.create_database_engine()
        self.session: Optional[Session] = None
    
    # Função para criar engine do banco de dados
    def create_database_engine(self) -> Engine:
        engine: Engine = create_engine(
            self.__connection_url, connect_args={'check_same_thread': False}
        )
        return engine
    
    # Função para obter a engine do banco de dados
    def get_engine(self) -> Engine:
        return self.__engine
    
    def __enter__(self):
        # Cria a sessão do banco de dados
        session_make = sessionmaker(
            bind=self.__engine, connect_args={"check_same_thread": False}
        )
        self.session = session_make()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            self.session.close()