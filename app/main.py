from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from views.url_routes import url_router
from views.page_routes import page_router
from views.user_routes import user_router
from models.__all_models import *

app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), name='static')
app.include_router(page_router)
app.include_router(user_router)
app.include_router(url_router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)