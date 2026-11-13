from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.user_service import UserService

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/")
def get_all_users(db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_all_user_service()