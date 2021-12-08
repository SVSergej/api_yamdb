from rest_framework import serializers
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from reviews.models import Title

from .category import CategorySerializer
from .genre import GenreSerializer



class TitleInputSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.IntegerField()

    class Meta:
        model = Title
        fields = ('id', 'name', 'year', 'genre',
                  'category', 'description', 'rating')

    def year_validator(value):
        if value > timezone.now().year:
            raise ValidationError(
                _('%(value)s is not a correcrt year!'),
                params={'value': value},)
