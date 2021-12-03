from rest_framework import serializers

from .genre import GenreSerializer
from .category import CategorySerializer


class InputSerializer(serializers.Serializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    name = serializers.StringRelatedField(read_only=True)
    year = serializers.IntegerField(read_only=True)
    description = serializers.StringRelatedField(read_only=True)
    id = serializers.ReadOnlyField()
    rating = serializers.IntegerField()

    class Meta:
        fields = ('id', 'name', 'year', 'genre',
                  'category', 'description', 'rating')
