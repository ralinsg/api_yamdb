from rest_framework import serializers
from reviews.models import Category, Comment, Genre, Title, Review, User
from rest_framework.validators import UniqueValidator


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
        fields = ('username', 'email')


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
    """Сериализует данные для получения, добавления и удаления категорий."""

    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    """Сериализует данные для получения.добавления и удаления жанров."""
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleSerializer(serializers.ModelSerializer):

    """Сериализует данные для добавления и получени информации о произведении
    А также для частичного обновления и удаления информации о произведении
    """

    genre = serializers.SlugRelatedField(
        slug_field='slug', many=True, queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug', queryset=Category.objects.all()
    )

    class Meta:
        model = Title
        fields = ('__all__')


class ReadTitleSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)
    category = CategorySerializer()
    rating = serializers.IntegerField(read_only=True)

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating', 'description', 'genre', 'category'
        )


class ReviewSerializer(serializers.ModelSerializer):
    """Сериализатор для отзывов."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'score', 'pub_date')
        model = Review

    def validate_score(self, value):
        if value is None or value not in range(1, 11):
            raise serializers.ValidationError(
                'Укажите оценку в виде целого числа от 1 до 10')
        return value

    def validate(self, data):
        if self.context['request'].method == 'POST':
            title_id = (
                self.context['request'].parser_context['kwargs']['title_id']
            )
            author = self.context['request'].user
            if Review.objects.filter(author=author, title=title_id).exists():
                raise serializers.ValidationError(
                    'Пользователь может оставить только 1 отзыв '
                    'на произведение')
        return data


class CommentSerializer(serializers.ModelSerializer):
    """Сериализатор для комментариев."""

    author = serializers.SlugRelatedField(
        read_only=True, slug_field='username'
    )

    class Meta:
        fields = ('id', 'text', 'author', 'pub_date')
        model = Comment
