# app/models/user.py

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    hashed_password = Column(String, nullable=False)
    is_active = Column(Boolean, default=True)

    profile = relationship("Profile", uselist=False, back_populates="user")
    experiences = relationship("Experience", back_populates="user", cascade="all, delete")
    educations = relationship("Education", back_populates="user", cascade="all, delete")
    skills = relationship("Skill", back_populates="user", cascade="all, delete-orphan")
