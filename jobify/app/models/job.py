# app/models/job.py

from sqlalchemy import Column, Integer, String, Text, DateTime, func
from app.database import Base

class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)
    company = Column(String(100), nullable=True)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
