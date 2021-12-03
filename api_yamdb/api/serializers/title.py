from rest_framework import serializers
from reviews.models import Title
import datetime as dt


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'genre', 'category', 'titles_reviews')

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год!')
        return value
