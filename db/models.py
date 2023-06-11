from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from datetime import datetime

from db.database import Base


class Question(Base):
    __tablename__ = 'questions'

    id: Mapped[int] = mapped_column(primary_key=True)
    question_uuid: Mapped[int]
    question: Mapped[str]
    answer: Mapped[str]
    created_at: Mapped[datetime] = mapped_column(default=datetime.utcnow)