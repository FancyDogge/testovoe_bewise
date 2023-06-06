from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

from db.database import Base


class Question(Base):
    __tablename__ = 'questions'
    # mapped_column
    id = Column(Integer, primary_key=True, index=True)
    question = Column(String)
    answer = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)