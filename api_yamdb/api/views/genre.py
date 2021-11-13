from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Genre
from ..serializers.genre import GenreSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = GenreSerializer



