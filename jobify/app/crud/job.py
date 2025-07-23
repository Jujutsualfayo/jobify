from sqlalchemy.orm import Session
from app.models.job import Job
from app.schemas.job import JobCreate, JobOut


def create_job(db: Session, job: JobCreate) -> Job:
    db_job = Job(**job.dict())
    db.add(db_job)
    db.commit()
    db.refresh(db_job)
    return db_job


def get_all_jobs(db: Session):
    return db.query(Job).all()


def get_job_by_id(db: Session, job_id: int):
    return db.query(Job).filter(Job.id == job_id).first()


def update_job(db: Session, job_id: int, job_data: JobCreate):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if db_job:
        for key, value in job_data.dict().items():
            setattr(db_job, key, value)
        db.commit()
        db.refresh(db_job)
    return db_job


def delete_job(db: Session, job_id: int):
    db_job = db.query(Job).filter(Job.id == job_id).first()
    if db_job:
        db.delete(db_job)
        db.commit()
    return db_job
