from sqlalchemy.orm import declarative_base

# Classe base para definições de classe declarativas
Base = declarative_base()
# URL do banco de dados
DB_URL: str = 'sqlite:///sqlite.db'

