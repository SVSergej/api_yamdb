from rest_framework import viewsets

from reviews.models import Genre
from ..serializers.genre import GenreSerializer
from .category import ViewsMixin


class GenreViewSet(ViewsMixin, viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer


def my_year_validator(value):
    if value > dt.datetime.now().year:
        raise ValidationError(
            _('%(value)s is not a correcrt year!'),
            params={'value': value},
        )
