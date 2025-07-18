from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class ResumeEvaluation(Base):
    __tablename__ = "resume_evaluations"

    id = Column(Integer, primary_key=True, index=True)
    resume_text = Column(Text)
    jd_text = Column(Text)
    ats_score = Column(Integer)
    created_at = Column(DateTime)
