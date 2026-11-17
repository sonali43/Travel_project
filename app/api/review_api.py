from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.service.review_service import ReviewService
from app.schema.review_schema import ReviewSchema,ReviewUpdate,ReviewResponse

review_router=APIRouter(prefix="/review",tags=["/Review"])

@review_router.post("/",response_model=ReviewResponse)
def create_review(review_data:ReviewSchema,db:Session=Depends(get_db)):
    service=ReviewService(db)
    return service.create_review(review_data)

@review_router.get("/{review_id}",response_model=ReviewResponse)
def get_review_by_id(review_id:int,db:Session=Depends(get_db)):
    service=ReviewService(db)
    return service.get_review_by_id(review_id)

@review_router.get("/",response_model=ReviewResponse)
def get_all_review(db:Session=Depends(get_db)):
    service=ReviewService(db)
    return service.get_all_review()

@review_router.get("/{place_id}",response_model=ReviewResponse)
def get_review_by_place_id(place_id:int,db:Session=Depends(get_db)):
    service=ReviewService(db)
    return service.get_review_by_place_id(place_id)

@review_router.put("/{review_id}",response_model=ReviewResponse)
def update_review(review_id:int,db:Session=Depends(get_db)):
    service=ReviewService(db)
    return service.update_review(review_id)

@review_router.delete("/{review_id}",response_model=ReviewResponse)
def delete_review(review_id:int,db:Session=Depends(get_db)):
    service=ReviewService(db)
    return service.delete_review(review_id)