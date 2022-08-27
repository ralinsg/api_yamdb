from django.contrib import admin

from .models import Category, Genre, Title, Token, User


class TokenAdmin(admin.ModelAdmin):
    list_display = ('pk', 'user', 'token')


class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'username', 'email', 'bio', 'role')
    search_fields = ('bio',)
    list_filter = ('username',)
    empty_value_display = '-пусто-'


admin.site.register(User, UserAdmin)
admin.site.register(Token, TokenAdmin)
admin.site.register(Category)
admin.site.register(Genre)
admin.site.register(Title)
