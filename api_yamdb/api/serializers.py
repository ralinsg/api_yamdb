from rest_framework import serializers
from yamdb.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):
    slug = serializers.SlugRelatedField(
        slug_field='categories',
        read_only=True,
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    slug = serializers.SlugRelatedField(
        slug_field='genres',
        read_only=True,
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Genre


class TitleSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset= Genre.objects.all(),
        slug_field='genres',
        many=True
    )
    category = serializers.SlugRelatedField(
        queryset= Category.objects.all(),
        slug_field='category',
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Title
