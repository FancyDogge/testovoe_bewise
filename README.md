## Описание
### Тестовое задание от компании Bewise, задача 1:
Был реализован сервис, позволяющий запрашивать заданное кол-во вопросов от API с викторинами.
Сервис проверяет уникальность полученных от API вопросов, есл вопрос уже существует в бд, то он не записывается, а к API делаются дополнительные запросы с количеством вопросов = колчичеству не записанных вопросов.

Для реализации проекта были использованы следующие технологии: FastAPI, SQLAlchemy, Docker, PostgreSQL (полный список в requirements.txt).


## Инструкция по запуску
Для начала нужно клонировать данный репозиторий

```
git clone https://github.com/FancyDogge/testovoe_bewise.git
```

Далее для запуска перейдите в директорию с docker-compose.yml и введите сдледующую команду для сборки проекта

```
docker-compose up --build
```

Начнется сборка образов и установка зависимостей, после чего должны запуститься приложение и бд.
Для простоты сборки, запуск миграций также произойдет автоматически.

Все готово!
Теперь приложение запущено и можно посмотреть документацию и опробовать API по адресу localhost:8000/docs

POST запрос можно сделать к адресу http://localhost:8000/questions любым удобным вам способом, со следующим json payload:

```
{
  "questions_num": 1
}
```

Где 1 - любое нужное вам число.
Пример с использованием curl:
```
curl -X POST -H "Content-Type: application/json" -d '{"questions_num": 5}' http://localhost:8000/questions
```
