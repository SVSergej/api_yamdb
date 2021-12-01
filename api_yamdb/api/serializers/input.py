# from typing_extensions import Required
from rest_framework import serializers

from .genre import GenreSerializer
from .category import CategorySerializer
# from rest_framework.decorators import api_view, permission_classes
# from rest_framework.permissions import AllowAny


class InputSerializer(serializers.Serializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    name = serializers.StringRelatedField(read_only=True)
    year = serializers.IntegerField(read_only=True)
    description = serializers.StringRelatedField(read_only=True)
    id = serializers.ReadOnlyField()

    class Meta:
        fields = ('id', 'name', 'year', 'genre',
                  'category', 'description', 'titles_reviews')