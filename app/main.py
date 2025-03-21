from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from views.routes import router
from models.__all_models import *

app = FastAPI()
app.mount('/static', StaticFiles(directory='app/static'), name='static')
app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)