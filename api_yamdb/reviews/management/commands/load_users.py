import os
from csv import DictReader
from django.core.management import BaseCommand
from api_yamdb.settings import BASE_DIR
from reviews.models import User

DATA_PATH = os.path.join(BASE_DIR, 'static/data')
FILENAME = 'users.csv'


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload users data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    """"Загрузка данных о пользователях из csv."""

    # Show this when the user types help
    help = 'Loads data from users.csv'

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if User.objects.exists():
            print('users data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print('Loading users data')
        users_data = os.path.join(DATA_PATH, FILENAME)

        # Code to load the data into database
        for line in DictReader(open(users_data)):
            user = User(
                pk=line['id'], username=line['username'],
                email=line['email'], role=line['role'], bio=line['bio']
            )
            user.save()
