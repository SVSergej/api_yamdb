from rest_framework import serializers
from api_yamdb.reviews.models import Categories


class CategoriesSerializer(serializers.ModelSerializer):
    titles = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:

        model = Categories
        fields = ('id', 'name', 'slug', 'titles')
