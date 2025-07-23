from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import get_db
from app.models.education import Education
from app.schemas.education import EducationCreate, EducationOut
from app.models.user import User
from app.dependencies.auth import get_current_user

router = APIRouter()

@router.post("/", response_model=EducationOut)
def create_education(education: EducationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_edu = Education(**education.dict(), user_id=current_user.id)
    db.add(db_edu)
    db.commit()
    db.refresh(db_edu)
    return db_edu

@router.get("/", response_model=list[EducationOut])
def list_educations(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Education).filter(Education.user_id == current_user.id).all()
