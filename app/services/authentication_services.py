from fastapi import Depends, HTTPException, status, Request
from sqlalchemy.orm import Session
from services.db_services import session_local
from passlib.context import CryptContext
from typing import Optional, Union, Any
from datetime import datetime, timedelta
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt, ExpiredSignatureError
import os

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
ACCESS_TOKEN_EXPIRE_MINUTES = 30 
ALGORITHM = "HS256"
JWT_SECRET_KEY = os.environ['JWT_SECRET_KEY']
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/login_user')

# Função para criptografar senha do usuário
def hash_password(password: str) -> str:
    return pwd_context.hash(password)

# Função para verificar senha segura
def verify_password(plain_password: str, hashed_password: str) -> bool:
    return pwd_context.verify(plain_password, hashed_password)

def create_access_token(
        subject: Union[str, Any],
        expires_delta: Optional[int] = None) -> str:
    if expires_delta is not None:
        expires = datetime.utcnow() + timedelta(expires_delta)
    else:
        expires = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    
    to_encode = {'exp': expires, 'sub': str(subject)}
    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, ALGORITHM)
    return encoded_jwt

# Função de autenticação obrigatória
def get_current_user(request: Request):
    token = request.cookies.get("access_token") 
    if not token:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Não autenticado. Faça login para acessar.",
        )
    
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        return {"user_id": payload["sub"]}
    except ExpiredSignatureError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token expirado. Faça login novamente.",
        )
    except JWTError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Token inválido. Faça login para acessar.",
        )

# função de autenticação opcional
def get_current_user_optional(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return None

    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[ALGORITHM])
        user_id = payload.get("sub")
        if not user_id:
            return None
        return {"user_id": user_id}
    except JWTError:
        return None

