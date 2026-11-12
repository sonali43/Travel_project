from pydantic import BaseModel, ConfigDict
from datetime import datetime

class WishlistSchema(BaseModel):
    users_id:int
    place_id:int
    
class WishlistRespone(BaseModel):
    id:int
    users_id:int
    place_id:int
    created_at:datetime
    
    model_config=ConfigDict(from_attributes=True)