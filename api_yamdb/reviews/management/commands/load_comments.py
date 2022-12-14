import os
from csv import DictReader
from django.core.management import BaseCommand
from api_yamdb.settings import BASE_DIR
from reviews.models import Comment, Review, User

DATA_PATH = os.path.join(BASE_DIR, 'static/data')
FILENAME = 'comments.csv'


ALREDY_LOADED_ERROR_MESSAGE = """
If you need to reload comments data from the CSV file,
first delete the db.sqlite3 file to destroy the database.
Then, run `python manage.py migrate` for a new empty
database with tables"""


class Command(BaseCommand):
    """"Загрузка данных об отзывах из csv."""

    # Show this when the user types help
    help = 'Loads data from comments.csv'

    def handle(self, *args, **options):

        # Show this if the data already exist in the database
        if Comment.objects.exists():
            print('comments data already loaded...exiting.')
            print(ALREDY_LOADED_ERROR_MESSAGE)
            return

        # Show this before loading the data into the database
        print('Loading comments data')
        comments_data = os.path.join(DATA_PATH, FILENAME)

        # Code to load the data into database
        for line in DictReader(open(comments_data)):
            review = Review.objects.filter(pk=line['review_id'])
            if review.exists():
                author = User.objects.filter(pk=line['author'])
                if author.exists():
                    comment = Comment(
                        pk=line['id'], review=review[0], text=line['text'],
                        author=author[0], pub_date=line['pub_date']
                    )
                    comment.save()
                else:
                    print(f'Author with id {line["author"]} does not exists')
            else:
                print(f'Review with id {line["review_id"]} does not exists')
