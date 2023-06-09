from pydantic import BaseModel
from datetime import datetime


class QuestionRequest(BaseModel):
    questions_num: int

class QuestionResponse(BaseModel):
    question_uuid: int
    question: str
    answer: str
    created_at: datetime