from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class ApplicationCreate(BaseModel):
    job_id: int
    user_id: int
    cover_letter: Optional[str] = None

class ApplicationOut(BaseModel):
    id: int
    job_id: int
    user_id: int
    cover_letter: Optional[str]
    created_at: datetime

    class Config:
        orm_mode = True
