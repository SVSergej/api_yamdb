from rest_framework import serializers
from api_yamdb.reviews.models import Genres


class GenresSerializer(serializers.ModelSerializer):
    titles = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:

        model = Genres
        fields = ('id', 'name', 'slug', 'titles')
