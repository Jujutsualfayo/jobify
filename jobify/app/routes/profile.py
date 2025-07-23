from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from fastapi import File, UploadFile
import shutil
import os
from uuid import uuid4


from app.schemas.profile import ProfileCreate, ProfileUpdate, ProfileOut
from app.models.user import User
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.crud import profile as profile_crud
from app.models.profile import Profile


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
UPLOAD_DIR = "static/uploads/profiles"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload-photo", response_model=ProfileOut)
def upload_profile_photo(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = db.query(Profile).filter(Profile.user_id == current_user.id).first()
    if not profile:
        raise HTTPException(status_code=404, detail="Profile not found")

    filename = f"{uuid4().hex}_{file.filename}"
    file_path = os.path.join(UPLOAD_DIR, filename)

    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    profile.profile_photo = f"/{file_path}"
    db.commit()
    db.refresh(profile)

    return profile