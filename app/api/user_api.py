from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.user_service import UserService
from app.schema.user_schema import UserSchema,UserUpdate,UserResponse

user_router = APIRouter(prefix="/users", tags=["Users"])


@user_router.post("/",response_model=UserResponse)
def create_user(user_data:UserSchema,db:Session=Depends(get_db)):
    service=UserService(db)
    return service.create_user_service(user_data)

@user_router.get("/{user_id}",response_model=UserResponse)
def get_user_by_id(user_id:int, db: Session = Depends(get_db)):
    service = UserService(db)
    return service.get_user_by_id(user_id)

@user_router.get("/{email_id}", response_model=UserResponse)
def get_user_by_email_id(email_id:str,db:Session=Depends(get_db)):
    service=UserService(db)
    return service.get_user_by_email(email_id)

@user_router.get("/",response_model=UserResponse)
def get_all_user(db:Session=Depends(get_db)):
    service=UserService(db)
    return service.get_all_user()

@user_router.put("/{user_id}", response_model=UserResponse)
def update_user(user_id:int,user_data=UserUpdate,db:Session=Depends(get_db)):
    service= UserService(db)
    return service.update_user(user_id,user_data)

@user_router.delete("/{user_id}", response_model=UserResponse)
def delete_user(user_id: int,db: Session = Depends(get_db)):
    service = UserService(db)
    return service.delete_user(user_id)