from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Genre
from ..serializers.genre import GenreSerializer
from ..permissions import AdminOrReadOnly


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = GenreSerializer
    permission_classes = (AdminOrReadOnly,)



