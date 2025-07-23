from sqlalchemy.orm import Session
from app.models.profile import Profile
from app.schemas.profile import ProfileCreate, ProfileUpdate

def create_profile(db: Session, user_id: int, profile_data: ProfileCreate):
    profile = Profile(user_id=user_id, **profile_data.dict())
    db.add(profile)
    db.commit()
    db.refresh(profile)
    return profile

def get_profile_by_user_id(db: Session, user_id: int):
    return db.query(Profile).filter(Profile.user_id == user_id).first()

def update_profile(db: Session, user_id: int, profile_data: ProfileUpdate):
    profile = get_profile_by_user_id(db, user_id)
    if profile:
        for key, value in profile_data.dict(exclude_unset=True).items():
            setattr(profile, key, value)
        db.commit()
        db.refresh(profile)
    return profile
