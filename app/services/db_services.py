from core.database import DBConnectionHandler
from sqlalchemy.orm import Session
from typing import Optional

# obtem a sessão do banco de dados
def session_local():
    with DBConnectionHandler() as db:
        return db.session
      