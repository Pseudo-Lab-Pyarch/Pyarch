from fastapi import FastAPI
from routers import house_router

app = FastAPI()

app.include_router(house_router.router)

@app.get('/')
async def root():
    return {"message": "Hello World"}
