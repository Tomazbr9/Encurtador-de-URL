from fastapi import FastAPI
from views.home_view import router
from models.__all_models import *

app = FastAPI()
app.include_router(router, prefix='/api')

if __name__ == '__main__':
    import uvicorn
    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)