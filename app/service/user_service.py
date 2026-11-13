from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.user_repo import UserRepository
from app.schema.user_schema import UserSchema, UserUpdate

class UserService:
    def __init__(self,db:Session):
        self.repo=UserRepository(db)
        
    def create_user_service(self,user_data:UserSchema):
        existing=self.repo.get_user_by_email(user_data.email)
        if existing:
            raise HTTPException(
                status_code=400,
                detail="Email already exists"
            )
        return self.repo.create_user(user_data)
    
    def get_user_by_id(self,user_id:int):
        user=self.repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return user
    
    def get_user_by_email(self,email_id:str):
        user=self.repo.get_user_by_email(email_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return user
    
    def get_all_user(self):
        return self.repo.get_all_user()
    
    def update_user(self,user_id:int,user_data:UserUpdate):
        user=self.repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        if user_data.email:
            existing=self.repo.get_user_by_email(user_data.email)
            if existing and existing.id != user_id:
                raise HTTPException(
                    status_code=400,
                    detail="Email already exists"
                )
        return self.repo.update_user(user_id,user_data)
    
    def delete_user(self,user_id:int):
        user=self.repo.get_user_by_id(user_id)
        if not user:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )
        return self.repo.delete_user(user_id)