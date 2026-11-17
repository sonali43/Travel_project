from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.review_repo import ReviewRepository
from app.schema.review_schema import ReviewSchema,ReviewUpdate

class ReviewService:
    def __init__(self, db:Session):
        self.repo=ReviewRepository(db)
        
    def create_review(self,review_data:ReviewSchema):
        return self.repo.create_review(review_data)
    
    def get_review_by_id(self, review_id:int):
        review = self.repo.get_review_by_id(review_id)
        if not review:
            raise HTTPException(
                status_code=404,
                detail="Review not found"
            )
        return review
    
    def get_all_review(self):
        return self.repo.get_all_review()
    
    def get_review_by_user_id(self, user_id:int):
        review=self.repo.get_review_by_user_id(user_id)
        if not review:
            raise HTTPException(
                status_code=404,
                detail="No reviews found for this user"
            )
        return review
    
    def get_review_by_place_id(self,place_id:int):
        review=self.repo.get_review_by_place_id(place_id)
        if not review:
            raise HTTPException(
                status_code=404,
                detail="No review found for this place"
            )
        return review
    
    def update_review(self,review_id:int,review_data:ReviewUpdate):
        review=self.repo.get_review_by_id(review_id)
        if not review:
            raise HTTPException(
                status_code=404,
                detail="Review not found"
            )
        return self.repo.update_review(review_id,review_data)
    
    def delete_review(self,review_id:int):
        review=self.repo.get_review_by_id(review_id)
        if not review:
            raise HTTPException(
                stat=404,
                detail="Review not found"
            )
        return self.repo.delete_review(review_id)
    