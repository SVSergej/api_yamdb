from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from reviews.models import Titles
from ..permissions import AdminOrReadOnly
from ..serializers import (
    TitlesSerializer,
    InputSerializer,
    OutputSerializer,
)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (AdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return InputSerializer

        return OutputSerializer
