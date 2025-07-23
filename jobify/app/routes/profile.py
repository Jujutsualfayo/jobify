from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.profile import ProfileCreate, ProfileUpdate, ProfileOut
from app.models.user import User
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.crud import profile as profile_crud

router = APIRouter()

@router.post("/", response_model=ProfileOut)
def create_my_profile(
    profile_data: ProfileCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    existing = profile_crud.get_profile_by_user_id(db, current_user.id)
    if existing:
        raise HTTPException(status_code=400, detail="Profile already exists")
    return profile_crud.create_profile(db, current_user.id, profile_data)

@router.get("/", response_model=ProfileOut)
def get_my_profile(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = profile_crud.get_profile_by_user_id(db, current_user.id)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile

@router.put("/", response_model=ProfileOut)
def update_my_profile(
    profile_data: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = profile_crud.update_profile(db, current_user.id, profile_data)
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")
    return profile
