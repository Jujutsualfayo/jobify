# app/schemas/job.py

from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class JobBase(BaseModel):
    title: str
    description: Optional[str] = None
    company: Optional[str] = None

class JobCreate(JobBase):
    pass

class JobOut(JobBase):
    id: int
    created_at: datetime

    class Config:
        orm_mode = True
