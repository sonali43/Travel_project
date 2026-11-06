from sqlalchemy import Integer,String,Float, ForeignKey,Text
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class Place(Base):
    __tablename__ = "place"
    
    id:Mapped[int]=mapped_column(
        Integer,primary_key=True,autoincrement=True,index=True
    )
    
    name:Mapped[str]=mapped_column(
        String(100),nullable=False
    )
    
    description:Mapped[str]=mapped_column(
        Text,nullable=False
    )
    
    address:Mapped[str]=mapped_column(
        String(250),nullable=False
    )
    
    city:Mapped[str]=mapped_column(
        String(100),nullable=False
    )
    
    state:Mapped[str]=mapped_column(
        String(100),nullable=False
    )
    
    estimated_cost:Mapped[float]=mapped_column(
        Float,nullable=False
    )
    
    latitude:Mapped[float]=mapped_column(
        Float,nullable=False
    )
    
    longitude:Mapped[float]=mapped_column(
        Float,nullable=False
    )
    
    category_id:Mapped[int]=mapped_column(
        ForeignKey("category.id"),nullable=False
    )
    
    category=relationship(
        "Category",
        back_populates="place"
    )
    
    review = relationship(
        "Review",
        back_populates="place"
    )
    
    wishlist=relationship(
        "Wishlist",
        back_populates="place"
    )