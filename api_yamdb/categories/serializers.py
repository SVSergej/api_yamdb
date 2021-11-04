from rest_framework import serializers 
from .models import Categories, Genres, Titles


class TitlesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Titles
        fields = '__all__'


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:

        model = Categories
        fields = '__all__'


class GenresSerializer(serializers.ModelSerializer):

    class Meta:

        model = Genres
        fields = '__all__'