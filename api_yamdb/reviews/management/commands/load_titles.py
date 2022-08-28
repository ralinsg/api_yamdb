import os
from csv import DictReader
from django.core.management import BaseCommand
from django.http import Http404
from django.shortcuts import get_object_or_404
from api_yamdb.settings import BASE_DIR
from reviews.models import Category, Genre, Title

DATA_PATH = os.path.join(BASE_DIR, 'static/data')
FILENAME = 'titles.csv'
GENRES_TITLES_FILENAME = 'genre_title.csv'


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload titles data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    """"Загрузка данных о произведениях из csv."""

    # Show this when the user types help
    help = 'Loads data from titles.csv'

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if Title.objects.exists():
            print('titles data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print('Loading titles data')
        titles_data = os.path.join(DATA_PATH, FILENAME)

        # Code to load the data into database
        for line in DictReader(open(titles_data)):
            try:
                category = get_object_or_404(Category, pk=line['category'])
                title = Title(
                    pk=line['id'], name=line['name'],
                    year=line['year'], category=category
                )
            except Http404:
                title = Title(
                    pk=line['id'], name=line['name'], year=line['year'],
                )
            title.save()

        print('Loading genres to titles')
        genres_titles_data = os.path.join(DATA_PATH, GENRES_TITLES_FILENAME)
        for line in DictReader(open(genres_titles_data)):
            try:
                title = get_object_or_404(Title, pk=line['title_id'])
                genre = get_object_or_404(Genre, pk=line['genre_id'])
                title.genre.add(genre)
            except Http404:
                print('Title or genre does not exists')
