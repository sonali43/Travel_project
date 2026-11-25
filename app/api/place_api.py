from fastapi import APIRouter , Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.schema.place_schema import PlaceSchema,PlaceResponse,PlaceUpdate
from app.service.place_service import PlaceService
from app.auth.auth_dependency import get_admin_user

place_router= APIRouter(prefix="/place",tags=["Place"])

@place_router.post("/",response_model=PlaceResponse)
def create_place(place_data:PlaceSchema,db:Session=Depends(get_db),current_data=Depends(get_admin_user)):
    service=PlaceService(db)
    return service.create_place(place_data,current_data)

@place_router.get("/{place_id}",response_model=PlaceResponse)
def get_place_by_id(place_id:int,db:Session=Depends(get_db)):
    service=PlaceService(db)
    return service.get_place_by_id(place_id)

@place_router.get("/{category_id}",response_model=PlaceResponse)
def get_place_by_category_id(category_id:int,db:Session=Depends(get_db)):
    service=PlaceService(db)
    return service.get_place_by_category_id(category_id)

@place_router.get("/",response_model=PlaceResponse)
def get_place_by_all(db:Session=Depends(get_db)):
    service=PlaceService(db)
    return service.get_place_by_all()

@place_router.get("/{city}",response_model=PlaceResponse)
def get_place_by_city(city:str,db:Session=Depends(get_db)):
    service=PlaceService(db)
    return service.get_place_by_city(city)

@place_router.get("/{state}",response_model=PlaceResponse)
def get_place_by_state(state:str,db:Session=Depends(get_db)):
    service=PlaceService(db)
    return service.get_place_by_state(state)

@place_router.put("/{place_id}", response_model=PlaceResponse)
def update_place(place_id:int,place_data=PlaceUpdate,db:Session=Depends(get_db),current_user=Depends(get_admin_user)):
    service= PlaceService(db)
    return service.update_place(place_id,place_data,current_user)

@place_router.delete("/{place_id}", response_model=PlaceResponse)
def delete_place(place_id: int,db: Session = Depends(get_db),current_user=Depends(get_admin_user)):
    service = PlaceService(db)
    return service.delete_place(place_id,current_user)