from pydantic import BaseModel
from datetime import datetime


class QuestionRequest(BaseModel):
    questions_num: int

class QuestionResponse(BaseModel):
    id: int
    question: str
    answer: str
    created_at: datetime