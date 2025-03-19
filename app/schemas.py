from pydantic import BaseModel, HttpUrl

# Criando modelo de validação 
class UrlModel(BaseModel):
    url: str 