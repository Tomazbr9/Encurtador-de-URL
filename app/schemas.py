from pydantic import BaseModel

class UserFields(BaseModel):
    username: str
    password: str