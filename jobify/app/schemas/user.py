# app/schemas/user.py

from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):  # Renamed from UserResponse
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True  # Pydantic v1 style
