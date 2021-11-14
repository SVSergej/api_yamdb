from rest_framework import serializers
from reviews.models import Titles
import datetime as dt


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ('id', 'name', 'year', 'genre', 'category')

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год!')
        return value
