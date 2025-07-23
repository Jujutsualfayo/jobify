# app/crud/skill.py

from sqlalchemy.orm import Session
from app.models.skill import Skill
from app.schemas.skill import SkillCreate

def create_skill(db: Session, skill: SkillCreate, user_id: int):
    db_skill = Skill(**skill.dict(), user_id=user_id)
    db.add(db_skill)
    db.commit()
    db.refresh(db_skill)
    return db_skill

def get_skills_by_user(db: Session, user_id: int):
    return db.query(Skill).filter(Skill.user_id == user_id).all()

def delete_skill(db: Session, skill_id: int, user_id: int):
    skill = db.query(Skill).filter(Skill.id == skill_id, Skill.user_id == user_id).first()
    if skill:
        db.delete(skill)
        db.commit()
    return skill
