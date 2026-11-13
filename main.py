from fastapi import FastAPI
from app.api.user_api import user_router



app = FastAPI()

app.include_router(user_router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}