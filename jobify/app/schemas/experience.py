from pydantic import BaseModel
from datetime import date
from typing import Optional

class ExperienceBase(BaseModel):
    title: str
    company: str
    location: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None
    description: Optional[str] = None

class ExperienceCreate(ExperienceBase):
    pass

class ExperienceOut(ExperienceBase):
    id: int
    class Config:
        orm_mode = True
