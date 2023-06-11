import requests
from sqlalchemy.orm import Session
from datetime import datetime

from db.models import Question
from schemas import QuestionRequest, QuestionResponse


def retrieve_questions(questions_num: QuestionRequest):
    saved_questions = []
    total_questions = 0

    while total_questions < questions_num:
        remaining_questions = questions_num - total_questions
        response = requests.get(f'https://jservice.io/api/random?count={remaining_questions}')
        if response.status_code == 200:
            data = response.json()
            for question_data in data:
                saved_questions.append(QuestionResponse(
                    question_uuid=question_data['id'],
                    question=question_data['question'],
                    answer=question_data['answer'],
                    created_at=datetime.strptime(question_data['created_at'], "%Y-%m-%dT%H:%M:%S.%fZ"),
                ))
                total_questions += 1

    return saved_questions


def filter_existing_questions(db: Session, saved_questions):
    new_questions = []
    for question in saved_questions:
        existing_question = db.query(Question).filter_by(question=question.question).first()
        if not existing_question:
            new_questions.append(Question(
                question_uuid=question.question_uuid,
                question=question.question,
                answer=question.answer,
                created_at=question.created_at,
            ))
    return new_questions


def write_new_questions(db: Session, new_questions):
    db.bulk_save_objects(new_questions)
    db.commit()