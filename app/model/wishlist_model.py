from datetime import datetime, timezone
from sqlalchemy import Integer,ForeignKey,DateTime,UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column,relationship
from app.db.database import Base

class Wishlist(Base):
    __tablename__="wishlist"
    
    __table_args__ =(UniqueConstraint("users_id","place_id", name="unique_user_wishlist"),)
    
    id:Mapped[int]=mapped_column(
        Integer,primary_key=True,index=True,autoincrement=True
    )
    
    users_id:Mapped[int]=mapped_column(
        ForeignKey("users.id"),nullable=False
    )
    
    place_id:Mapped[int]=mapped_column(
        ForeignKey("place.id"),nullable=False
    )
    
    created_at:Mapped[datetime] =mapped_column(
        DateTime,
        default=datetime.now(timezone.utc),
        nullable=False
    )
    
    users = relationship(
        "Users",
        back_populates="wishlist"
    )
    
    place=relationship(
        "Place",
        back_populates="wishlist"
    )