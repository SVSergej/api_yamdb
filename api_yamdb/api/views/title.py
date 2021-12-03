from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from django_filters.rest_framework import DjangoFilterBackend
from django.db.models import Avg

from reviews.models import Title, Review
from ..filters import TitleFilter
from ..permissions import AdminOrReadOnly
from ..serializers import (
    TitlesSerializer,
    InputSerializer,
    OutputSerializer,
)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.annotate(
        rating=Avg('reviews__score')).order_by('-year')
    serializer_class = TitlesSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filterset_class = TitleFilter

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return InputSerializer
        return OutputSerializer
