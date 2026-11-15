from fastapi import FastAPI
from app.api.user_api import user_router
from app.api.category_api import category_router


app = FastAPI()

app.include_router(user_router)
app.include_router(category_router)

@app.get("/")
async def root():
    return {"message": "Hello, World!"}