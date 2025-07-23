from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"), unique=True)
    full_name = Column(String, nullable=True)
    bio = Column(String, nullable=True)
    location = Column(String, nullable=True)
    skills = Column(String, nullable=True)  # Comma-separated string
    education = Column(String, nullable=True)
    experience = Column(String, nullable=True)

    user = relationship("User", back_populates="profile")
    profile_photo = Column(String, nullable=True)  # URL or path to the image
