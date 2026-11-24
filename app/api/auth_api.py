from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.auth_service import AuthService
from app.schema.auth_schema import  RegisterSchema, LoginSchema, TokenReponse

auth_router=APIRouter(prefix="/auth",tags=["Authentication"])

@auth_router.post("/register")
def ragister_user(user_data:RegisterSchema,db:Session=Depends(get_db)):
    service=AuthService(db)
    return service.register_user(user_data)

@auth_router.post("/login",response_model=TokenReponse)
def login_user(login_data:LoginSchema,db:Session=Depends(get_db)):
    service=AuthService(db)
    return service.login_user(login_data)