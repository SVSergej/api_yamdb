from rest_framework import filters, mixins, viewsets 
from reviews.models import Titles, Genre, Category
from .serializers import TitlesSerializer, CategorySerializer, GenreSerializer, InputSerializer, OutputSerializer
from .permissions import AdminOrReadOnly
from rest_framework.pagination import LimitOffsetPagination


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    pagination_class = LimitOffsetPagination
    # permission_classes = (AdminOrReadOnly,)

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return InputSerializer

        return OutputSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genre.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = GenreSerializer
