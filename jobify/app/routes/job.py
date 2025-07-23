from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.schemas.job import JobCreate, JobOut
from app.dependencies.auth import get_current_user
from app.models.user import User
from app.database import get_db
from app.crud import job as job_crud

router = APIRouter()

@router.post("/", response_model=JobOut)
def create_job(job: JobCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    job_with_owner = JobCreate(**job.dict())
    job_with_owner_dict = job_with_owner.dict()
    job_with_owner_dict["owner_id"] = current_user.id
    return job_crud.create_job(db=db, job=job_with_owner)

@router.get("/", response_model=list[JobOut])
def list_jobs(db: Session = Depends(get_db)):
    return job_crud.get_all_jobs(db=db)

@router.get("/{job_id}", response_model=JobOut)
def get_job(job_id: int, db: Session = Depends(get_db)):
    job = job_crud.get_job_by_id(db=db, job_id=job_id)
    if not job:
        raise HTTPException(status_code=404, detail="Job not found")
    return job
