from fastapi import Depends
from app.repo.user_repo import UserRepository
from app.service.user_service import UserService
from app.db.database import get_db

def get_user_service(db=Depends(get_db)):
    user_repository = UserRepository(db)
    user_service = UserService(user_repository)
    return user_service