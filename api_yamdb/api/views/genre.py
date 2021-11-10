from rest_framework import viewsets
from api_yamdb.reviews.models import Genres
from ..serializers.genres import GenresSerializer


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
