from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from services.db_services import session_local
from models.url_models import UserModel
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para criptografar senha
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Função para verificar senha segura
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

# Função para verificar se o usuario está authenticado
def get_current_user(request: Request) -> str:
    user = request.cookies.get('user')

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Usuário não authenticado'
        )
    return user