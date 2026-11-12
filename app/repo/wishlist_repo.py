from sqlalchemy.orm import Session
from app.model.wishlist_model import Wishlist
from app.schema.wishlist_schema import WishlistSchema

class WishlistRepository:
    def __tablename__(self,db:Session):
        self.db=db
        
    def create_wishlist(self,wishlit_data:WishlistSchema):
        new_wishlist=Wishlist(
            users_id=wishlit_data.users_id,
            place_id=wishlit_data.place_id
        )
        
        self.db.add(new_wishlist)
        self.db.commit()
        self.db.refresh(new_wishlist)
        
        return new_wishlist
    
    def get_wishlist_by_id(self,wishlist_id:int):
        return self.db.query(Wishlist).filter(Wishlist.id==wishlist_id).first()
    
    def get_wishlist_by_all(self):
        return self.db.query(Wishlist).all()
    
    def get_wishlist_by_users_id(self,users_id:int):
        return self.db.query(Wishlist).filter(Wishlist.users_id==users_id).all()
    
    def get_wishlist_by_place_id(self,place_id:int):
        return self.db.query(Wishlist).filter(Wishlist.place_id==place_id).all()
    
    def check_wishlist_exist(self,users_id:int, place_id:int):
        return self.db.query(Wishlist).filter(Wishlist.users_id==users_id, Wishlist.place_id==place_id).first()
    
    def delete_wishlist(self,wishlist_id:int):
        wishlist=self.get_wishlist_by_id(wishlist_id)
        if wishlist:
            self.db.delete(wishlist)
            self.db.commit()
        return wishlist
    
    def remove_place_from_wishlist(self,users_id:int, place_id:int):
        wishlist=self.check_wishlist_exist(users_id, place_id)
        if wishlist:
            self.db.delete(wishlist)
            self.db.commit()
        return wishlist