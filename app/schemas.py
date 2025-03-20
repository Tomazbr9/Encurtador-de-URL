from pydantic import BaseModel

# Criando modelo de validação 
class UrlModel(BaseModel):
    url: str 