
# Проект YaMDb

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).

## Структура работы:


## Технологический стек:

- Python 3
- Django
- Django Rest Framework
- PyJWT
- Simple JWT

## Установка проекта:

Клонировать репозиторий:

```bash
 git clone git@github.com:ralinsg/api_yamdb.git

```
Перейти в склонированный репозиторий:
```bash
 cd api_final_yatube
```
Cоздать виртуальное окружение:
```bash
py -3.7 -m venv venv 
```
Активировать виртуальное окружение:
```bash
 source venv/Scripts/activate
```
Установить зависимости из файла requirements.txt:
```bash
 pip install -r requirements.txt
```
Создать файл .env со следующими данными:
```bash
SECRET_KEY=<Ваш секретный ключ>
```

## Запуск проекта:

```bash
 python3 manage.py runserver
```
## Примеры запросов

Добавление новой категории(POST-запрос).

```bash
http://127.0.0.1:8000/api/v1/categories/
```

Получение списка всех жанров(GET-запрос).

```bash
http://127.0.0.1:8000/api/v1/genres/
```

Частичное обновление информации о произведении(PATCH-запрос)
 
 ```bash
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```
## Автор

- [@ralinsg](https://github.com/ralinsg)
- [@alexeyseven](https://github.com/Alexeyseven)
- [@elinagayduk](https://github.com/elinagayduk)
