import jwt
from fastapi import Depends,HTTPException
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.repo.user_repo import UserRepository
from app.auth.auth_utils import SECRET_KEY, ALGORITHM

oauth2_scheme  = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(
    token:str=Depends(oauth2_scheme),
    db:Session=Depends(get_db)
):
    credentials_exception = HTTPException(
        status_code=401,
        detail="Invalid or expired token",
        headers={"WW-Authenticate":"Bearer"}
    )
    
    try:
        payload=jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )
        
        user_id=payload.get("sub")
        if user_id is None:
            raise credentials_exception
        
    except jwt.InvalidTokenError:
        raise credentials_exception
    
    repo=UserRepository(db)
    user= repo.get_user_by_id(int(user_id))
    
    if user is None:
        raise credentials_exception
    
    return user