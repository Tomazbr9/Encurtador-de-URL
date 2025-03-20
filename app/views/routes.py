from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from models.url_models import Url
from schemas import UrlModel
from sqlalchemy.orm import Session
from services.db_services import session_local
from services.url_service import generate_code
from core.settings import TEMPLATES
from fastapi.requests import Request

router = APIRouter()

@router.get('/home', status_code=status.HTTP_200_OK)
async def home(request: Request):
    context = {
        'request': request
    }
    return TEMPLATES.TemplateResponse('home.html', context=context)

# Rota para encurtar url.
@router.post('/short', status_code=status.HTTP_201_CREATED)
async def shorten_url(
    long_url: UrlModel, 
    db: Session = Depends(session_local)) -> JSONResponse:

    # Gera código aleatorio.
    short_url = generate_code()
    
    # Verifica se o código gerado já existe, caso exista, gera outro codigo. 
    while db.query(Url).filter(Url.short_url == short_url).first():
        short_url = generate_code()
    
    new_url = Url(short_url=short_url, long_url=long_url.url)
    db.add(new_url)
    db.commit()
    
    # Retorna a url encurtada
    return JSONResponse(
        content={'short_url': f'http://localhost:8000/{short_url}'},
        status_code=status.HTTP_201_CREATED
    )

# Rota para redirecionar para url original
@router.get('/{short_url}', status_code=status.HTTP_200_OK)
async def redirect_url(
    short_url: str,
    db: Session = Depends(session_local)) -> RedirectResponse:
    
    # Verifica se já existe a url enviada no db, caso contrario, retorna None
    url = db.query(Url).filter(Url.short_url == short_url).first()

    if url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='URL não encontrada!')
    # Redireciona para a pagina da url original
    return RedirectResponse(url=str(url.long_url))
    

    
