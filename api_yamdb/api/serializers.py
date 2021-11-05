from rest_framework import serializers
from rest_framework.relations import SlugRelatedField

from api_yamdb.reviews.models import Review, Comments


class ReviewSerializer(serializers.ModelSerializer):
    title_id = SlugRelatedField(slug_field='title', read_only=True)
    score = SlugRelatedField(slug_field='score', read_only=True)

    def validate_score(self, score):
        message = 'error'
        if 0 < score < 11:
            return score
        return serializers.ValidationError(message)

    class Meta:
        fields = '__all__'
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        fields = '__all__'
        model = Comments
