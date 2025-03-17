from app.core.database import DBConnectionHandler
from app.core.settings import Base

# Criar todas as tabelas no banco de dados
engine = DBConnectionHandler()
Base.metadata.create_all(bind=engine.get_engine())
