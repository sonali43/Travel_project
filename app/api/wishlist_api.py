
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.wishlist_service import WishlistService
from app.schema.wishlist_schema import WishlistSchema, WishlistRespone



wishlist_router = APIRouter(prefix="/wishlists",tags=["Wishlist"])

@wishlist_router.post("/", response_model=WishlistRespone)
def create_wishlist(wishlist_data: WishlistSchema,db: Session = Depends(get_db)):
    service = WishlistService(db)
    return service.create_wishlist(wishlist_data)

@wishlist_router.get("/{wishlist_id}", response_model=WishlistRespone)
def get_wishlist_by_id(wishlist_id: int,db: Session = Depends(get_db)):
    service = WishlistService(db)
    return service.get_wishlist_by_id(wishlist_id)

@wishlist_router.get("/", response_model=list[WishlistRespone])
def get_wishlist_by_all(db: Session = Depends(get_db)):
    service = WishlistService(db)
    return service.get_wishlist_by_all()

@wishlist_router.get("/user/{users_id}", response_model=list[WishlistRespone])
def get_wishlist_by_users_id(users_id: int,db: Session = Depends(get_db)):
    service = WishlistService(db)
    return service.get_wishlist_by_users_id(users_id)

@wishlist_router.get("/place/{place_id}", response_model=list[WishlistRespone])
def get_wishlist_by_place_id(place_id: int,db: Session = Depends(get_db)):
    service = WishlistService(db)
    return service.get_wishlist_by_place_id(place_id)

@wishlist_router.get("/check/{users_id}/{place_id}", response_model=WishlistRespone)
def check_wishlist_exist(users_id: int,place_id: int,db: Session = Depends(get_db)):
    service = WishlistService(db)
    return service.check_wishlist_exist(users_id, place_id)

@wishlist_router.delete("/{wishlist_id}")
def delete_wishlist(wishlist_id: int, db: Session = Depends(get_db)):
    service = WishlistService(db)
    service.delete_wishlist(wishlist_id)
    return {"message": "Wishlist deleted successfully"}

@wishlist_router.delete("/user/{users_id}/place/{place_id}")
def remove_place_from_wishlist(users_id: int,place_id: int,db: Session = Depends(get_db)):
    service = WishlistService(db)
    service.remove_place_from_wishlist(users_id, place_id)
    return {"message": "Place removed from wishlist successfully"}
