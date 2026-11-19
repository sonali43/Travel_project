from fastapi import FastAPI
from app.api.user_api import user_router
from app.api.category_api import category_router
from app.api.place_api import place_router
from app.api.review_api import review_router
from app.api.wishlist_api import wishlist_router

app = FastAPI()

app.include_router(user_router)
app.include_router(category_router)
app.include_router(place_router)
app.include_router(review_router)
app.include_router(wishlist_router)


@app.get("/")
async def root():
    return {"message": "Hello, World!"}