from rest_framework import serializers

from reviews.models import Review


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True, slug_field=' username'
    )

    def validate_score(self, score):
        message = 'Оценка может ставиться от 1 до 10'
        if 0 < score < 11:
            return score
        raise serializers.ValidationError(message)

    def validate(self, data):
        message = 'Отзыв уже существует'
        if self.context['request'].method != 'POST':
            return data
        title = self.context['request'].parser_context['kwargs']['title_id']
        title_id = self.context['view'].kwargs.get('title_id')
        user = self.context['request'].user
        if Review.objects.filter(author=user, title=title):
            raise serializers.ValidationError(message)
        return data

    class Meta:
        fields = ['id', 'text', 'author', 'score', 'pub_date']
        model = Review
