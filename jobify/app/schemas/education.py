from pydantic import BaseModel
from datetime import date
from typing import Optional

class EducationBase(BaseModel):
    institution: str
    degree: str
    field_of_study: Optional[str] = None
    start_date: date
    end_date: Optional[date] = None

class EducationCreate(EducationBase):
    pass

class EducationOut(EducationBase):
    id: int
    class Config:
        orm_mode = True
