
# Проект YaMDb

Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles).

Регистрация пользователя реализована с помощью JWT-токена. 

Для автоматизации развертывания на сервере используется Docker, а для управления взаимодействием нескольких контейнеров применяется утилита docker-compose.

## Технологический стек:

- Python 3
- Django
- Django REST framework
- PostgreSQL
- Docker
- Gunicorn
- nginx
- Simple JWT
- GIT

## Установка и запуск проекта:

Клонировать репозиторий и перейти в него в командной строке:

``` bash
 git clone git@github.com:ralinsg/api_yamdb.git
```

``` bash
 cd api_yamdb
```

Cоздать и активировать виртуальное окружение:

``` bash
 py -3.7 -m venv venv
```

``` bash
 source venv/Scripts/activate
```

``` bash
 python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

``` bash
 pip install -r requirements.txt
```

Переходим в папку с файлом docker-compose.yaml:

``` bash
 cd infra
```

Поднимаем контейнеры (db, web, nginx)

``` bash
 docker-compose up -d --build
```

Выполнить миграции:

``` bash
 docker-compose exec web python manage.py migrate
```

Создаем суперпользователя:

``` bash
 docker-compose exec web python manage.py createsuperuser
```

Собираем статику:

``` bash
 docker-compose exec web python manage.py collectstatic --no-input
```

Создаем дамп (резервуню копию) базы:

``` bash
 docker-compose exec web python manage.py dumpdata > fixtures.json
```

Останавливаем контейнеры:

``` bash
 docker-compose down -v
```

Шаблон наполнения .env (не включен в текущий репозиторий) расположенный по пути infra/.env

``` bash
SECRET_KEY='secret_key'
DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
```

    
## Примеры запросов:

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

## Авторы

- Ралин Сергей [@ralinsg](https://github.com/ralinsg)
- Кузнецов Алексей [@alexeyseven](https://github.com/Alexeyseven)
- Гайдук Элина [@elinagayduk](https://github.com/elinagayduk)
