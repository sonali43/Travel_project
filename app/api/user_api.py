from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.user_service import UserService
from app.schema.user_schema import UserSchema,UserUpdate,UserResponse

router = APIRouter(prefix="/users", tags=["Users"])


@router.post("/")
def create_user(user_data:UserSchema,db:Session=Depends(get_db)):
    service=UserService(db)
    return service.create_user_service(user_data)

@router.get("/{user_id}")
def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_id(user_id)

@router.get_user_by_email("/email/{email_id}")
def get_user_by_email_id(email_id:str,db:Session=Depends(get_db)):
    service=UserService(db)
    return service.get_user_by_email(email_id)