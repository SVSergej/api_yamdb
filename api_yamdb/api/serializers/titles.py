from rest_framework import serializers
from api_yamdb.reviews.models import Genres, Titles
import datetime as dt
from .genres import GenresSerializer


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)

    class Meta:

        model = Titles
        fields = ('id', 'name', 'year', 'genre', 'category')

    def create(self, validated_data):

        genres = validated_data.pop('genre')
        title = Titles.objects.create(**validated_data)

        for genre in genres:
            current_genre, status = Genres.objects.get_or_create(
                **genre)

            Genre_Title.objects.create(
                genre=current_genre, title=title)
        return title

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год!')
        return value

