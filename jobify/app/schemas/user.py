# app/schemas/user.py

from pydantic import BaseModel, EmailStr

# Request schema for creating a new user
class UserCreate(BaseModel):
    username: str
    email: EmailStr
    password: str

# Response schema when returning a user
class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    is_active: bool

    class Config:
        orm_mode = True
