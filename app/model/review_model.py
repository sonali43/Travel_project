from datetime import datetime, timezone
from sqlalchemy import Integer, String, ForeignKey ,DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class Review(Base):
    __tablename__ = "review"
    
    id:Mapped[int]=mapped_column(
        Integer,primary_key=True, index=True,autoincrement=True
    )
    
    user_id:Mapped[int]=mapped_column(
        ForeignKey("users.id"),nullable=False
    )
    
    place_id:Mapped[int]=mapped_column(
        ForeignKey("place.id"),nullable=False
    )
    
    rating:Mapped[int]=mapped_column(
        Integer, nullable=False
    )
    
    comment:Mapped[str]=mapped_column(
        String(1000),nullable=False
    )
    
    created_at:Mapped[datetime]=mapped_column(
        DateTime(timezone=True),default=lambda: datetime.now(timezone.utc),nullable=False
    )
    
    users = relationship(
        "Users",
        back_populates="review"
    )
    
    place= relationship(
        "Place",
        back_populates="review"
    )