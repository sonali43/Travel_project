from pydantic import BaseModel, EmailStr

class RegisterSchema(BaseModel):
    name: str
    email :EmailStr
    password: str
    
    
class LoginSchema(BaseModel):
    email:EmailStr
    password:str
    
class TokenReponse(BaseModel):
    access_token: str
    token_type: str