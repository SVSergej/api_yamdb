from rest_framework import serializers

from api_yamdb.reviews.models import Category, Titles, Genre


class OutputSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )

    class Meta:
        model = Titles
        fields = ('name', 'year', 'genre', 'category')
