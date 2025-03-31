from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse, RedirectResponse
from fastapi.requests import Request

from sqlalchemy.orm import Session

from services.db_services import session_local
from services.url_services import generate_code, is_valid_url
from services.authentication_services import get_current_user_optional

from typing import Optional

from models.url_models import UrlModel, UserModel
from models.url_models import UserModel

from controllers.controllers import Controller

url_router = APIRouter()

# Rota para encurtar url.
@url_router.post('/short', status_code=status.HTTP_201_CREATED)
async def shorten_url(
    request: Request,
    user: Optional[UserModel] = Depends(get_current_user_optional),
    db: Session = Depends(session_local)) -> JSONResponse:
    
    data = await request.json()
    url: str =  data.get('url')

    # Verifica se a url é None ou uma string válida
    if not url or not isinstance(url, str):
        return JSONResponse(
            content={'message': 'A URL deve ser uma string válida!'},
            status_code=status.HTTP_400_BAD_REQUEST)
    
    # verifica se a url é válida
    if not is_valid_url(url):
        return JSONResponse(
            content={'message': 'URL inválida!'},
            status_code=status.HTTP_400_BAD_REQUEST
        )

    # Gera código aleatorio.
    short_url = generate_code()
    
    # Verifica se o código gerado já existe, caso exista, gera outro codigo. 
    while db.query(UrlModel).filter(UrlModel.short_url == short_url).first():
        short_url = generate_code()

    if user:
        new_url = UrlModel(short_url=short_url, long_url=url, user_id=user['user_id'])
        db.add(new_url)
        db.commit()
    
    # Retorna a url encurtada
    return JSONResponse(
        content={'short_url': f'http://localhost:8000/{short_url}'},
        status_code=status.HTTP_201_CREATED
    )

# Rota criada para deletar urls
@url_router.delete('/delete_url/{id}', status_code=status.HTTP_202_ACCEPTED)
async def delete_url(id: str, db: Session = Depends(session_local)):
    con = Controller(UrlModel)
    deleted = con.delete_register_crud(id, db)

    if not deleted:
        raise HTTPException(status_code=404, detail="URL não encontrada")
    return JSONResponse(content={'message': 'Url deletada com sucesso'})

# Rota para redirecionar para url original
@url_router.get('/{short_url}', status_code=status.HTTP_200_OK)
async def redirect_url(
    short_url: str,
    db: Session = Depends(session_local)) -> RedirectResponse:

    # Verifica se já existe a url enviada no db, caso contrario, retorna None
    url = db.query(UrlModel).filter(UrlModel.short_url == short_url).first()
    
    if url is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail='URL não encontrada!')
    # Redireciona para a pagina da url original
    return RedirectResponse(url=str(url.long_url))




    
