from rest_framework import serializers
from reviews.models import Category, Genre, Titles, Genre_Title
import datetime as dt


class CategorySerializer(serializers.ModelSerializer):
    titles = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:

        model = Category
        fields = ('id','name','slug')


class GenreSerializer(serializers.ModelSerializer):
    titles = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:

        model = Genre
        fields = ('id','name', 'slug')


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True)

    class Meta:

        model = Titles
        fields = ('id', 'name', 'year', 'genre', 'category')
    
    def create(self, validated_data):

        genres = validated_data.pop('genre')
        title = Titles.objects.create(**validated_data)

        for genre in genres:

            current_genre, status = Genre.objects.get_or_create(
                **genre)

            Genre_Title.objects.create(
                genre=current_genre, title=title)
        return title
    
    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год!')
        return value
