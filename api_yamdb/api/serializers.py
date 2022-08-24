from rest_framework import serializers
from yamdb.models import Category, Genre, Title


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ('id',)
        lookup_field = 'slug'
        extra_kwargs = {
            'url': {'lookup_field': 'slug'}
        }


class GenreSerializer(serializers.ModelSerializer):

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
