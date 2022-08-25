# Проект YaMDb

------------
### Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).

------------
### Технологии
- requests==2.26.0
- django==2.2.16
- djangorestframework==3.12.4
- PyJWT==2.1.0
- pytest==6.2.4
- pytest-django==4.4.0
- pytest-pythonpath==0.7.3
- djangorestframework-simplejwt==4.7.2

------------


### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ralinsg/api_yamdb.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source venv/Scripts/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

------------
### Примеры запросов
 Добавление новой категории(POST-запрос).
```
http://127.0.0.1:8000/api/v1/categories/
```
Получение списка всех жанров(GET-запрос).
```
http://127.0.0.1:8000/api/v1/genres/
```
Частичное обновление информации о произведении(PATCH-запрос)
```
http://127.0.0.1:8000/api/v1/titles/{titles_id}/
```
------------

### Авторы
- Алексей Кузнецов
- Сергей Ралин
- Элина Гайдук
