from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.user_repo import UserRepository
from app.schema.user_schema import UserSchema
from app.schema.auth_schema import RegisterSchema,LoginSchema
from app.auth.auth_utils import hash_password, verify_password, create_access_token

class AuthService:
    def __init__(self,db:Session):
        self.repo=UserRepository(db)
        
    def register_user(self, user_data:RegisterSchema):
        existing_user=self.repo.get_user_by_email(user_data.email)
        if existing_user:
            raise HTTPException(
                status_code=400,
                detail="Email already registered"
            )
            
        hashed_password=hash_password(user_data.password)
        
        new_user_data=UserSchema(
            name=user_data.name,
            email=user_data.email,
            password=hashed_password
        )
        
        return self.repo.create_user(new_user_data)
    
    def login_user(self, login_data:LoginSchema):
        user=self.repo.get_user_by_email(login_data.email)
        if not user:
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
        if not verify_password(login_data.password, user.password):
            raise HTTPException(
                status_code=401,
                detail="Invalid email or password"
            )
            
        access_token=create_access_token(
            date={
                "sub":str(user.id),
                "role":user.role
            }
        )
        
        return {
            "access_token":access_token,
            "token_type":"bearer"
            }