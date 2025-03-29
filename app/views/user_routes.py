from fastapi import APIRouter, Depends, Request, status, HTTPException
from fastapi.responses import JSONResponse, Response
from sqlalchemy.orm import Session
from models.url_models import UserModel
from services.db_services import session_local
from services.authentication_services import hash_password, verify_password, create_access_token

user_router = APIRouter()

# Rota para criar usuário
@user_router.post('/register_user', status_code=status.HTTP_201_CREATED)
async def create_user(
    request: Request,
    db: Session = Depends(session_local)) -> JSONResponse:

    data = await request.json()
    username: str = data.get('username')
    password: str = data.get('password')   
    
    # Verifica se usuario ja existe
    existing_user = db.query(UserModel).filter(
        UserModel.username == username).first()
    
    if existing_user:
        return JSONResponse(
            content={'message':'Usuário já existe!'},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    
    new_user = UserModel(
        username=username,
        password=hash_password(password))
    
    db.add(new_user)
    db.commit()

    return JSONResponse(
        content={'message': 'Usuário criado com sucesso!'},
        status_code=status.HTTP_201_CREATED
    )

# Rota para processar login
@user_router.post('/login_user', status_code=status.HTTP_200_OK)
async def login_user(
    request: Request,
    db: Session = Depends(session_local)) -> JSONResponse:
    
    data = await request.json()
    
    username: str = data.get('username')
    password: str = data.get('password')

    # Busca usuario no banco de dados
    user = db.query(UserModel).filter(
        UserModel.username == username).first()
    
    # Verifica se o usuário existe e se a senha está correta
    if not user or not verify_password(password, str(user.password)):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Usuário ou senha inválidos",
        )
    
    access_token: str = create_access_token(user.id)
    
    # Cria a resposta e armazena o token no cookie HTTP-only
    response = JSONResponse({"message": "Login bem sucedido!"})
    response.set_cookie(
        key="access_token", 
        value=access_token,
        httponly=True, 
        max_age=60 * 30,
        secure=True 
    )
    
    return response

@user_router.get('/logout', status_code=status.HTTP_200_OK)
async def logout(response: Response):
    response.delete_cookie("access_token")
    return {'message': 'logout bem sucedido!'}
