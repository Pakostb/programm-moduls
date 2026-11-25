# Flask + MySQL: регистрация + Lesson 14 (структуры данных)

## Что сделано

### Lesson 15 — Регистрация
- GET /register — форма
- POST /register — создание пользователя через db.create_user()
- Успех → session + profile.html
- Ошибка (дубль / пустые поля) → register.html с текстом ошибки
- Есть логин и выход

### Lesson 14 — Структуры данных
Файл data_structures.py — все 5 заданий + assert-проверка.

## Как запустить

### 1. База данных
mysql -u root -p < schema.sql
(или выполни содержимое schema.sql в Workbench / DBeaver)

### 2. Зависимости
pip install flask pymysql

### 3. Flask
python main.py
Открой http://127.0.0.1:8080

### 4. Структуры данных
python data_structures.py

## Настройки БД
По умолчанию: host=localhost, user=root, password=admin, database=flask_auth
Поменяй в database.py при необходимости.
