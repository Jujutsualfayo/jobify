from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.experience import Experience
from app.schemas.experience import ExperienceCreate, ExperienceOut
from app.models.user import User
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=ExperienceOut)
def create_experience(experience: ExperienceCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_exp = Experience(**experience.dict(), user_id=current_user.id)
    db.add(db_exp)
    db.commit()
    db.refresh(db_exp)
    return db_exp

@router.get("/", response_model=list[ExperienceOut])
def list_experiences(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Experience).filter(Experience.user_id == current_user.id).all()
