from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.place_repo import PlaceRepository
from app.schema.place_schema import PlaceSchema,PlaceUpdate

class PlaceService:
    def __init__(self,db:Session):
        self.repo=PlaceRepository(db)
        
    def create_place(self,place_date:PlaceSchema):
        return self.repo.create_place(place_date)
    
    def get_place_by_id(self,place_id:int):
        place=self.repo.get_place_by_id(place_id)
        if not place:
            raise HTTPException(
                status_code=404,
                detail="Place not found"
            )
        return place
    
    def get_place_by_all(self):
        return self.repo.get_place_by_all()
    
    def get_place_by_category_id(self,category_id:int):
        place=self.repo.get_place_by_category_id(category_id)
        if not place:
            raise HTTPException(
                status_code=404,
                deta="No place found by category id"
            )
        return place
    
    def get_place_by_city(self,city:str):
        place=self.repo.get_place_by_city(city)
        if not place:
            raise HTTPException(
                status_code=404,
                detail="No places found in this city"
            )
        return place
    
    def get_place_by_state(self,state:str):
        place=self.repo.get_place_by_state(state)
        if not place:
            raise HTTPException(
                status_code=404,
                detail="No place found in this state"
            )
        return place
    
    def update_place(self,place_id:int,place_date:PlaceUpdate):
        place=self.repo.get_place_by_id(place_id)
        if not place:
            raise HTTPException(
                status_code=404,
                detail="Place not found"
            )
        return self.repo.update_place(place_id,place_date)
    
    def delete_place(self,place_id:int):
        place=self.repo.get_place_by_id(place_id)
        if not place:
            raise HTTPException(
                status_code=404,
                detail="Place not found"
            )
        return self.repo.delete_place(place_id)