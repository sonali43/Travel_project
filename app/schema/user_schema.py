from pydantic import BaseModel, EmailStr, ConfigDict


class UserSchema(BaseModel):
    name: str
    email: EmailStr
    password: str
    
class UserResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    role: str
    
    model_config=ConfigDict(from_attributes=True)
    
    
class UserUpdate(BaseModel):
    name: str
    email: EmailStr
    password: str