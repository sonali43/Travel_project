from sqlalchemy.orm import Session
from fastapi import HTTPException
from app.repo.wishlist_repo import WishlistRepository
from app.schema.wishlist_schema import WishlistSchema

class WishlistService:
    def __init__(self, db:Session):
        self.repo=WishlistRepository(db)
        
    def create_wishlist(self,wishlist_date:WishlistSchema):
        existing=self.repo.check_wishlist_exist(wishlist_date.users_id,wishlist_date.place_id)
        if existing :
            raise HTTPException(
                status_code=400,
                detail="This place is already in the user's wishlist"
            )
        return self.repo.create_wishlist(wishlist_date)
    
    def get_wishlist_by_id(self,withlist_id:int):
        wishlist=self.repo.get_wishlist_by_id(withlist_id)
        if not wishlist:
            raise HTTPException(
                status_code=404,
                detail="Wishlist not found"
            )
        return wishlist
    
    def get_wishlist_by_all(self):
        return self.repo.get_wishlist_by_all()
    
    def get_wishlist_by_user_id(self,user_id:int):
        wishlist=self.repo.get_wishlist_by_users_id(user_id)
        if not wishlist:
            raise HTTPException(
                status_code=404,
                detail="No wishlist items found for this user"
            )
        return wishlist
    
    def get_wishlist_by_place_id(self,place_id:int):
        wishlist=self.repo.get_wishlist_by_place_id(place_id)
        if not wishlist:
            raise HTTPException(
                status_code=404,
                detail="No wishlist item found for this place"
            )
        return wishlist
    
    def check_wishlist_exist(self,user_id:int,place_id:int):
        wishlist=self.repo.check_wishlist_exist(user_id,place_id)
        if not wishlist:
            raise HTTPException(
                status_code=404,
                detail="This place is not in the user's wishlist" 
            )
        return wishlist
    
    def delete_wishlist(self, wishlist_id: int):
        wishlist = self.repo.get_wishlist_by_id(wishlist_id)

        if not wishlist:
            raise HTTPException(
                status_code=404,
                detail="Wishlist not found"
            )

        return self.repo.delete_wishlist(wishlist_id)

    
    def remove_place_from_wishlist(self, users_id: int, place_id: int):
        wishlist = self.repo.check_wishlist_exist(users_id, place_id)

        if not wishlist:
            raise HTTPException(
                status_code=404,
                detail="This place is not in the user's wishlist"
            )

        return self.repo.remove_place_from_wishlist(users_id, place_id)
  
        