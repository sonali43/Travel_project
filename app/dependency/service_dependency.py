from fastapi import Depends
from app.repo.user_repo import UserRepository
from app.service.user_service import UserService
from app.repo.category_repo import CategoryRepo
from app.service.category_service import CategoryService
from app.db.database import get_db

def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service

def get_category_Service(db=Depends(get_db)):
    category_repo= CategoryRepo(db)
    category_service=CategoryService(category_repo)
    return category_service

