from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class Education(Base):
    __tablename__ = "educations"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    institution = Column(String, nullable=False)
    degree = Column(String, nullable=False)
    field_of_study = Column(String)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date)

    user = relationship("User", back_populates="educations")
