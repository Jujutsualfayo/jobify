from pydantic import BaseModel
from typing import Optional

class ProfileBase(BaseModel):
    full_name: Optional[str] = None
    bio: Optional[str] = None
    location: Optional[str] = None
    skills: Optional[str] = None  # Comma-separated for now
    education: Optional[str] = None
    experience: Optional[str] = None

class ProfileCreate(ProfileBase):
    pass

class ProfileUpdate(ProfileBase):
    pass

class ProfileOut(ProfileBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True
