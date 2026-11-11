from sqlalchemy.orm import Session
from app.model.review_model import Review
from app.schema.review_schema import ReviewSchema,ReviewUpdate

class ReviewRepository:
    def __init__(self,db:Session):
        self.db=db
        
    def create_review(self,review_data:ReviewSchema):
        new_review=Review(
            user_id=review_data.user_id,
            place_id=review_data.place_id,
            rating=review_data.rating,
            comment=review_data.comment
        )
        
        self.db.add(new_review)
        self.db.commit()
        self.db.refresh(new_review)
        
        return new_review
    
    def get_review_by_id(self,review_id:int):
        return self.db.query(Review).filter(Review.id==review_id).first()
    
    def get_all_review(self):
        return self.db.query(Review).all()
    
    def get_review_by_user_id(self,user_id:int):
        return self.db.query(Review).filter(Review.user_id==user_id).all()
    
    def get_review_by_place_id(self,place_id:int):
        return self.db.query(Review).filter(Review.place_id==place_id).all()
    
    def update_review(self,review_id:int,review_data:ReviewUpdate):
        review = self.get_review_by_id(review_id)
        
        if review:
            update_data=review_data.model_dump(exclude_unset=True)
            for key, value in update_data.items():
                setattr(review,key,value)
                
            self.db.commit()
            self.db.refresh(review)
            
        return review
    
    def delete_review(self,review_id:int):
        review=self.get_review_by_id(review_id)
        if review:
            self.db.delete(review)
            self.db.commit()
            
        return review