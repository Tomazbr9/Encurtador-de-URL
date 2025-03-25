from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse, Response, RedirectResponse
from schemas import UserFields
from sqlalchemy.orm import Session
from models.url_models import UserModel
from core.settings import TEMPLATES
from services.db_services import session_local
from services.authentication_services import hash_password, verify_password

user_router = APIRouter()

# Rota para criar usuário
@user_router.post('/create_user', status_code=status.HTTP_201_CREATED)
async def create_user(
    create_user: UserFields,
    request: Request,
    db: Session = Depends(session_local)) -> JSONResponse:
    
    # Verifica se usuario ja existe
    existing_user = db.query(UserModel).filter(
        UserModel.username == create_user.username).first()
    
    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail='Usuário já existe!'
        )
    
    new_user = UserModel(
        username=create_user.username,
        password=hash_password(create_user.password))
    
    db.add(new_user)
    db.commit()

    return JSONResponse(
        content={'message': 'Usuário criado com sucesso!'},
        status_code=status.HTTP_201_CREATED
    )

# Rota para processar login
@user_router.post('/login_user', status_code=status.HTTP_200_OK)
async def login_user(
    response: Response,
    request: Request,
    db: Session = Depends(session_local)) -> JSONResponse:

    data = await request.json()
    username: str = data.get('username')
    password: str = data.get('password')

    # Busca usuario no banco de dados
    user = db.query(UserModel).filter(
        UserModel.username == username).first()
    
    # Verifica se o usuario existe
    if not user or not verify_password(password, str(user.password)):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, 
            detail='Usuário ou senha inválidos'
        )
    
    # insere dados do usuario nos cookies
    response.set_cookie(key='username', value=str(user.username), httponly=True)
    return JSONResponse(
        content={'message': 'login bem sucedido!'},
        status_code=status.HTTP_200_OK)

@user_router.get('/logout')
async def logout(response: Response):
    response.delete_cookie('username')
    return RedirectResponse(url='/login_page')
