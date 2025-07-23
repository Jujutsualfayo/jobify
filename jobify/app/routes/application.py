from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.application import ApplicationCreate, ApplicationOut
from app.models.application import Application
from app.database import get_db
from app.dependencies.auth import get_current_user
from app.models.user import User

router = APIRouter()

@router.post("/", response_model=ApplicationOut)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    db_app = Application(user_id=current_user.id, **application.dict())
    db.add(db_app)
    db.commit()
    db.refresh(db_app)
    return db_app

@router.get("/", response_model=list[ApplicationOut])
def list_my_applications(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Application).filter(Application.user_id == current_user.id).all()
