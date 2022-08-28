import os
from csv import DictReader
from django.core.management import BaseCommand
from api_yamdb.settings import BASE_DIR
from reviews.models import Category

DATA_PATH = os.path.join(BASE_DIR, 'static/data')
FILENAME = 'category.csv'


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload categories data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    """"Загрузка данных о категориях из csv."""

    # Show this when the user types help
    help = 'Loads data from category.csv'

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if Category.objects.exists():
            print('categories data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print('Loading categories data')
        categories_data = os.path.join(DATA_PATH, FILENAME)

        # Code to load the data into database
        for line in DictReader(open(categories_data)):
            category = Category(
                pk=line['id'], name=line['name'], slug=line['slug']
            )
            category.save()
