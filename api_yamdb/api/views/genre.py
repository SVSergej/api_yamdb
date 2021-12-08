from rest_framework import filters, status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from reviews.models import Genre

from ..permissions import AdminOrReadOnly
from ..serializers.genre import GenreSerializer
from .category import ViewsMixin

class GenreViewSet(ViewsMixin, viewsets.ModelViewSet):
    queryset = Genre.objects.all()  
    serializer_class = GenreSerializer
