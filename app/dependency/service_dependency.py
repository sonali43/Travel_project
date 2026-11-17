from fastapi import Depends
from app.repo.user_repo import UserRepository
from app.service.user_service import UserService
from app.repo.category_repo import CategoryRepo
from app.service.category_service import CategoryService
from app.repo.place_repo import PlaceRepository
from app.service.place_service import PlaceService
from app.repo.review_repo import ReviewRepository
from app.service.review_service import ReviewService
from app.db.database import get_db

def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service

def get_category_service(db=Depends(get_db)):
    category_repo= CategoryRepo(db)
    category_service=CategoryService(category_repo)
    return category_service

def get_place_service(db=Depends(get_db)):
    place_repo=PlaceRepository(db)
    place_service=PlaceService(place_repo)
    return place_service

def get_review_service(db=Depends(get_db)):
    review_repository=ReviewRepository(db)
    review_service=ReviewService(review_repository)
    return review_service