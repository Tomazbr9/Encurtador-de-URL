from fastapi import FastAPI, HTTPException, status, Response

app = FastAPI()


@app.get('/', status_code=status.HTTP_200_OK)
async def home():
    return Response(content='Sucesso', status_code=status.HTTP_200_OK)

if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='main:app', host='0.0.0.0', port=8000, reload=True)