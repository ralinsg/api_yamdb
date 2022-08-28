import os
from csv import DictReader
from django.core.management import BaseCommand
from django.http import Http404
from django.shortcuts import get_object_or_404
from api_yamdb.settings import BASE_DIR
from reviews.models import Review, Title, User

DATA_PATH = os.path.join(BASE_DIR, 'static/data')
FILENAME = 'review.csv'


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload reviews data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    """"Загрузка данных об отзывах из csv."""

    # Show this when the user types help
    help = 'Loads data from review.csv'

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if Review.objects.exists():
            print('reviews data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print('Loading reviews data')
        reviews_data = os.path.join(DATA_PATH, FILENAME)

        # Code to load the data into database
        for line in DictReader(open(reviews_data)):
            try:
                title = get_object_or_404(Title, pk=line['title_id'])
                author = get_object_or_404(User, pk=line['author'])
                score = int(line['score'])
                if score not in range(1, 11):
                    print('Incorrect score')
                else:
                    review = Review(
                        pk=line['id'], title=title, text=line['text'],
                        author=author, score=score, pub_date=line['pub_date']
                    )
                    review.save()
            except Http404:
                print('Title or author does not exists')
