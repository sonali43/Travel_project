from sqlalchemy import Integer, String, Enum as SQLEnum
from app.enum.enum import UserRole
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
    
    role: Mapped[UserRole] = mapped_column(
        SQLEnum(UserRole, name="user_role"),
        default=UserRole.USER,
        nullable=False
    )

    
    review = relationship(
        "Review",
        back_populates="users"
    )
    
    wishlist = relationship(
        "Wishlist",
        back_populates="users"
    )