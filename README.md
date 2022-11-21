# Проект YaMDb

------------
### Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).

------------
### Технологии

- asgiref==3.2.10
- requests==2.26.0
- django==2.2.16
- djangorestframework==3.12.4
- PyJWT==2.1.0
- pytest==6.2.4
- pytest-django==4.4.0
- pytest-pythonpath==0.7.3
- djangorestframework-simplejwt==4.7.2
- django-filter==2.4.0
- gunicorn==20.0.4
- psycopg2-binary==2.8.6
- pytz==2020.1
- sqlparse==0.3.1


------------

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:ralinsg/infra_sp2.git
```

```
cd infra_sp2
```

Cоздать и активировать виртуальное окружение:

```
py -3.7 -m venv env
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

Переходим в папку с файлом docker-compose.yaml:

```
cd infra
```

Поднимаем контейнеры (db, web, nginx)

```
docker-compose up -d --build
```

Выполнить миграции:

```
docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Собираем статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Создаем дамп (резервуню копию) базы:

```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Останавливаем контейнеры:

```
docker-compose down -v
```

Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env

```
SECRET_KEY='secret_key'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
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
- Сергей Ралин
