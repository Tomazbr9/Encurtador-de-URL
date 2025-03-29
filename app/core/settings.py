from sqlalchemy.orm import declarative_base
from fastapi.templating import Jinja2Templates
from fastapi.security import HTTPBasic

# Classe base para definições de classes declarativas
Base = declarative_base()
# URL do banco de dados
DB_URL: str = 'sqlite:///sqlite.db'
# Define o diretorio dos templates
TEMPLATES = Jinja2Templates(directory='app/templates')



