from fastapi import APIRouter, status, Request, Depends

from sqlalchemy.orm import Session

from core.settings import TEMPLATES
from services.db_services import session_local
from models.url_models import UserModel
from services.authentication_services import get_current_user, get_current_user_optional

page_router = APIRouter()

# rota para home no front end
@page_router.get('/home', status_code=status.HTTP_200_OK)
async def home(request: Request, user = Depends(get_current_user_optional)):
    context = {
        'request': request,
        'user': user,
        'title': 'Home'
    }
    return TEMPLATES.TemplateResponse('home.html', context=context)

# rota para pagina de login no front end
@page_router.get('/login', status_code=status.HTTP_200_OK)
async def login(request: Request):
    context = {
        'request': request,
        'message_top': 'Por favor, faça login',
        'title': 'Login',
        'btn_name': 'Login',
        'id_form': 'formLogin'
    }
    return TEMPLATES.TemplateResponse('auth.html', context=context)

# rota para pagina de login no front end
@page_router.get('/register', status_code=status.HTTP_200_OK)
async def register(request: Request):
    context = {
        'request': request,
        'message_top': 'Registre-se',
        'title': 'Register',
        'btn_name': 'Registrar',
        'id_form': 'formRegister'
    }
    return TEMPLATES.TemplateResponse('auth.html', context=context)

# rota protegida para acessar historico de urls
@page_router.get('/historic', status_code=status.HTTP_200_OK)
async def historic(
    request: Request,
    user: dict = Depends(get_current_user),
    db: Session = Depends(session_local)
    ):

    user = db.query(UserModel).filter(
        UserModel.id == user['user_id']
    ).first()
    
    # obtem todas as urls vinculadas ao usuário logado
    urls = user.urls if user else None

    context = {
        'request': request,
        'urls': urls,
        'user': user,
        'title': 'historic'
    }

    return TEMPLATES.TemplateResponse('historic.html', context=context)