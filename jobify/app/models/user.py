# app/models/user.py

from sqlalchemy import Column, String, Integer, Boolean
from app.database import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    profile = relationship("Profile", uselist=False, back_populates="user")
    experiences = relationship("Experience", back_populates="user", cascade="all, delete")
    educations = relationship("Education", back_populates="user", cascade="all, delete")




    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)
