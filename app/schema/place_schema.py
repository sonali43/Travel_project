from pydantic import BaseModel, ConfigDict, Field

class PlaceSchema(BaseModel):
    name:str
    description:str
    address:str
    city:str
    state:str
    estimated_cost:float=Field(ge=0)
    latitude:float=Field(ge=-90,le=90)
    longitudde: float = Field(ge=-180, le=180)
    category_id:int
    
class PlaceUpdate(BaseModel):
    name:str | None=None
    description:str |None=None
    address:str |None=None
    city:str | None=None
    state:str|None=None
    estimated_cost:float |None=Field(default=None, ge=0)
    latitude:float |None=Field(default=None, ge= -90, le=90)
    longitude:float |None=Field(default=None, ge=-180, le=180)
    category_id |None=None
    
class PlaceResponse(BaseModel):
    id:int
    name:str
    description:str
    address:str
    city:str
    state:str
    estimated_cost:float
    latitude:float
    longitude:float
    category_id:int
    
    model_config=ConfigDict(from_attributes=True)