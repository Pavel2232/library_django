# 📓📖Backend библиотеки.Django + Django ORM + DRF + MySQL + Celery + Redis + Flower
Backend - Developer - Тестовое Задание
Необходимо разработать Django-приложение для управления книгами в библиотеке.
Реализовать задачи:
- Rest API с базовым CRUD фунĸционалом для ĸниг.
- Cоздайте модель для хранения информации о пользователях приложения.
- Добавить эндпоинт для регистрации нового пользователя.
- Используя Celery, реализуйте асинхронную задачу,
которая отправляет приветственное электронное письмо пользователю при его регистрации.
При создании нового пользователя, задача Celery должна запускаться асинхронно для отправки приветственного письма.
* Endpoints:
```http request
GET /api/books/
- списоĸ ĸниг
```
```http request
GET /api/books/{book_id}
- выдать информацию по ĸонĸретной ĸниге
```
```http request
POST /api/books/
- создание ĸниги
```
```http request
DELETE /api/books/{book_id}
- удаление ĸниги
```
```http request
PUT /api/books/{book_id}
- изменение ĸниги
```
```http request
PATCH /api/books/{book_id}
- частичное изменение ĸниги
```
```http request
POST /users/signup/
- регистрация пользователя
```
# [Swagger](https://editor-next.swagger.io)
```swagger codegen
https://raw.githubusercontent.com/Pavel2232/library_django/new_test_work/library%20API.yaml
- Вставить ссылку на сайте Swagger
```
# Локальный Swagger
```http request
GET api/schema/swagger-ui/
```

## Как запустить

* Скачайте код ```git clone https://github.com/Pavel2232/library_django/tree/new_test_work```
* Заполните .env
```dotenv
- SECRET_KEY= секретный ключ приложения джанго
- DATABASE_URL= mysql://имя:пароль@адрес бд/название бд. для проверки используйте(psql://test:test@127.0.0.1:5432/test)
- ALLOWED_HOSTS=localhost,127.0.0.1
- DATABASE_URL=mysql://test:test@127.0.0.1:3306/test
- REDIS_URL=redis://localhost:6379/0
- EMAIL_HOST=YOUR_EMAIL_HOST
- EMAIL_HOST_USER=YOUR_EMAIL_HOST_USER
- EMAIL_HOST_PASSWORD=YOUR_EMAIL_HOST_PASSWORD
- EMAIL_PORT=YOUR_EMAIL_PORT
```
```docker
Выполните команду docker-compose up
```
```python
./manage.py runserver
```
