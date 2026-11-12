from sqlalchemy.orm import Session
from app.model.place_model import Place
from app.schema.place_schema import PlaceSchema,PlaceUpdate

class PlaceRepository:
    def __tablename__ (self,db:Session):
        self.db=db
        
    def create_place(self,place_date:PlaceSchema):
        new_place=Place(
            name=place_date.name,
            description=place_date.description,
            address=place_date.address,
            city=place_date.city,
            state=place_date.state,
            estimated_cost=place_date.estimated_cost,
            latitude=place_date.latitude,
            longitude=place_date.longitudde,
            category_id=place_date.category_id
        )
        
        self.db.add(new_place)
        self.db.commit()
        self.db.refresh(new_place)
        
        return new_place
    
    def get_place_by_id(self,place_id:int):
        return self.db.query(Place).filter(Place.id==place_id).first()
    
    def get_place_by_all(self):
        return self.db.query(Place).all()
    
    def get_place_by_category_id(self,category_id:int):
        return self.db.query(Place).filter(Place.category_id==category_id).all()
    
    def get_place_by_city(self,city:str):
        return self.db.query(Place).filter(Place.city.ilike(f"%{city}%")).all()
    
    def get_place_by_state(self,state:str):
        return self.db.query(Place).filter(Place.state.ilike(f"%{state}%")).all()
    
    def update_place(self,place_id:int,place_date:PlaceUpdate):
        place=self.get_place_by_id.items(place_id)
        if place:
            update_data=place_date.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(place, key, value)
                
            self.db.commit()
            self.db.refresh(place)
            
        return place
    
    def delete_place(self,place_id:int):
        place=self.get_place_by_id(place_id)
        if place:
            self.db.delete(place)
            self.db.commit()
        return place