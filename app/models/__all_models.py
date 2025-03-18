from core.database import DBConnectionHandler
from core.settings import Base

# Criar todas as tabelas no banco de dados
engine = DBConnectionHandler()
Base.metadata.create_all(bind=engine.get_engine())
