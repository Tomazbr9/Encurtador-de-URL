from fastapi import Depends, HTTPException, status
from fastapi.security import HTTPBasicCredentials
from sqlalchemy.orm import Session
from models.url_models import UserModel
from services.db_services import session_local
from passlib.context import CryptContext
from core.settings import SECURITY
from typing import Optional

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# Função para criptografar senha do usuário
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Função para verificar senha segura
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def get_current_user(
        credentials: HTTPBasicCredentials = Depends(SECURITY),
        db: Session = Depends(session_local)
    ) -> UserModel | HTTPException:
    
    user = db.query(UserModel).filter(UserModel.username == credentials.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='Usuário não encontrado'
        )
    
    return user

def get_current_user_optional():

    try:
        user = Depends(get_current_user)
        return user
    except HTTPException:
        return None

