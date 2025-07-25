# app/routes/skill.py

from fastapi import APIRouter, Depends, HTTPException
from app.schemas import skill
from sqlalchemy.orm import Session
from typing import List

from app import crud, schemas, models
from app.database import get_db
from app.dependencies.auth import get_current_user

router = APIRouter(prefix="/skills", tags=["Skills"])

@router.post("/", response_model=skill.Skill)
def create_skill(
    skill: schemas.skill.SkillCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return crud.skill.create_skill(db, skill, current_user.id)

@router.get("/", response_model=List[schemas.skill.Skill])
def read_skills(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    return crud.skill.get_skills_by_user(db, current_user.id)

@router.delete("/{skill_id}", response_model=schemas.skill.Skill)
def delete_skill(
    skill_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user),
):
    skill = crud.skill.delete_skill(db, skill_id, current_user.id)
    if not skill:
        raise HTTPException(status_code=404, detail="Skill not found")
    return skill
