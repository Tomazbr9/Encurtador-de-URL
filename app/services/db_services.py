from core.database import DBConnectionHandler
from sqlalchemy.orm import Session
from typing import Optional

def session_local() -> Optional[Session]:
    with DBConnectionHandler() as db:
        return db.session
      