from sqlalchemy.orm import Session
from app.model.user_model import Users

class UserRepository:
    
    def __init__(self, db:Session):
        self.db=db
        
    def create_user(self,user_data):
        new_user=Users(
            name=user_data.name,
            email=user_data.email,
            password=user_data.password,
            role=user_data.role
        )
        
        self.db.add(new_user)
        self.db.commit()
        self.db.refresh(new_user)
        
        return new_user
    
    def get_user_by_id(self,user_id:int):
        return self.db.query(Users).filter(Users.id==user_id).first()
    
    def get_user_by_email(self,email:str):
        return self.db.query(Users).filter(Users.email==email).first()
    
    def get_all_user(self):
        user=self.get_user_by_id(user)
    
    def update_user(self,user_id:int,user_data):
        user=self.get_user_by_id(user_id)
        
        if user:
            user.name = user_data.name
            user.email=user_data.email
            user.password= user_data.password
            
            self.db.commit()
            self.db.refresh(user)
            
        return user
    
    def delete_user(self,user_id:int):
        user=self.get_user_by_id(user_id)
        
        if user:
            self.db.delete(user)
            self.db.commit()
            
        return user 