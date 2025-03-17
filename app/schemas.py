from pydantic import BaseModel, HttpUrl

# Criando modelo de validação 
class CreateUrl(BaseModel):
    url: HttpUrl 