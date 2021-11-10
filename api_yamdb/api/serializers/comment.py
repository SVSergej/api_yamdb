from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from api_yamdb.reviews.models import Comments


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comments
