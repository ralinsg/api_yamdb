from django.contrib import admin
from yamdb.models import Category, Genre, Title, User

admin.site.register(User)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
