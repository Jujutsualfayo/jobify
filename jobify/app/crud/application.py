from sqlalchemy.orm import Session
from app.models.application import Application
from app.schemas.application import ApplicationCreate


def create_application(db: Session, application: ApplicationCreate) -> Application:
    db_application = Application(**application.dict())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application


def get_all_applications(db: Session):
    return db.query(Application).all()


def get_application_by_id(db: Session, application_id: int):
    return db.query(Application).filter(Application.id == application_id).first()


def get_applications_by_user_id(db: Session, user_id: int):
    return db.query(Application).filter(Application.user_id == user_id).all()


def delete_application(db: Session, application_id: int):
    db_application = db.query(Application).filter(Application.id == application_id).first()
    if db_application:
        db.delete(db_application)
        db.commit()
    return db_application
