from fastapi import APIRouter, status, Request
from core.settings import TEMPLATES

page_router = APIRouter()

# rota para home no front end
@page_router.get('/home', status_code=status.HTTP_200_OK)
async def home(request: Request):
    context = {
        'request': request
    }
    return TEMPLATES.TemplateResponse('home.html', context=context)

# rota para pagina de login no front end
@page_router.get('/login', status_code=status.HTTP_200_OK)
async def login(request: Request):
    context = {
        'request': request
    }
    return TEMPLATES.TemplateResponse('login.html', context=context)