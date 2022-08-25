from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from reviews.models import Category, Genre, Title, User


class SignUpSerializer(serializers.ModelSerializer):
    """Сериализует данные для странички создания пользователя"""

    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        required=True,
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    def validate_username(self, user_username):
        if user_username.lower() == 'me':
            raise serializers.ValidationError("Username 'me' is not valid")
        return user_username

    class Meta:
        model = User
        fields = ("username", "email")


class JWTokenSerializer(serializers.Serializer):
    """Сериализует данные для странички получения jwt-токена"""

    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    """Сериализатор для просмотра списка пользователей,
    добавления, редактирования, удаления отдельного
    пользователя"""

    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        required=True,
    )

    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        model = User
        fields = (
            'username', 'email',
            'first_name', 'last_name', 'bio', 'role')


class ProfileSerializer(serializers.ModelSerializer):
    """Сериализует данные для личного профиля пользователя"""

    class Meta:
        model = User
        fields = (
            'username', 'email',
            'first_name', 'last_name', 'bio', 'role')
        read_only_fields = ('role', )


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id',)
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        exclude = ('id',)
        lookup_field = 'slug'

class TitleSerializer(serializers.ModelSerializer):

    class Meta:
        fields = '__all__'
        model = Title
