from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from typing import List

from db.database import get_db
from utils import retrieve_questions, filter_existing_questions, write_new_questions
from schemas import QuestionRequest, QuestionResponse


app = FastAPI()


@app.post("/questions", response_model=List[QuestionResponse])
def get_questions(request: QuestionRequest, db: Session = Depends(get_db)):
    questions_num = request.questions_num

    # отдельно собираем вопросы
    saved_questions = retrieve_questions(questions_num)
    # фильтруем существующие вопросы
    new_questions = filter_existing_questions(db, saved_questions)
    # отдельно пишем в бд
    write_new_questions(db, new_questions)

    return saved_questions















# @app.post("/questions", response_model=List[QuestionResponse])
# def get_questions(request: QuestionRequest, db: Session = Depends(get_db)):
#     questions_num = request.questions_num
#     saved_questions = []

#     while len(saved_questions) < questions_num:
#         response = requests.get(f'https://jservice.io/api/random?count={questions_num}')
#         if response.status_code == 200:
#             data = response.json()

#             for question_data in data:
#                 # Проверяем существует ли полеченный вопрос в бд
#                 # Все взаимодействия с дб в отдельный файл
#                 existing_question = db.query(Question).filter_by(question=question_data['question']).first()
#                 if existing_question:
#                     continue

#                 # Создаем новый объект и сохраняем его в бд
#                 new_question = Question(
#                     question=question_data['question'],
#                     answer=question_data['answer']
#                 )
#                 # вытащить все вопросы из полученного списка
#                 # разделить получение и запись данных
#                 db.add(new_question)
#                 db.commit()

#                 # добавляем сохраненный объект в лист для респонса
#                 saved_questions.append(QuestionResponse(
#                     id=new_question.id,
#                     question=new_question.question,
#                     answer=new_question.answer,
#                     created_at=new_question.created_at,
#                 ))
#     # если возвращать нечего - вернется пустой объект
#     if saved_questions:
#         return saved_questions
#     else:
#         return {}


# перенести алембик в db
# дополнить докер
# в докерфайле также установить зависимость для pydub
# перенести логику некоторую в отдельный файл schemas.py, например