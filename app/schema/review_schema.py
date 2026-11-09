from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class ReviewSchema(BaseModel):
    user_id:int
    place_id:int
    rating:int=Field(ge=1,le=5)
    comment:str
    
class ReviewUpdate(BaseModel):
    reating:int|None=Field(default=None,ge=1,le=5)
    comment:str|None=None

class ReviewResponse(BaseModel):
    id:int
    user_id:int
    place_id:int
    rating:int
    comment:str
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)