from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped,mapped_column, relationship

from app.db.database import Base

class Users(Base):
    __tablename__ = "users"
    
    id:Mapped[int] = mapped_column(
        Integer, primary_key=True,index=True,autoincrement=True
    )
    
    name:Mapped[str] =mapped_column(
        String(150),nullable=False
    )
    
    email : Mapped[str] = mapped_column(
        String(150),unique=True,nullable=False,index=True
    )
    
    password:Mapped[str]=mapped_column(
        String(255),nullable=False
    )
    
    role:Mapped[str]=mapped_column(
        String(20),default="users",nullable=False
    )
    
    review = relationship(
        "Review",
        back_populates="users"
    )
    
    wishlist = relationship(
        "Wishlist",
        back_populates="users"
    )