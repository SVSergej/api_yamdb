from rest_framework import serializers
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from reviews.models import Category, Genre, Title


class TitleOutputSerializer(serializers.ModelSerializer):
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
        model = Title
        fields = '__all__'
    

    def year_validator(value):
        if value > timezone.now().year:
            raise ValidationError(
                _('%(value)s is not a correcrt year!'),
                params={'value': value},)
