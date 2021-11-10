from rest_framework import filters, mixins, permissions, viewsets 
from reviews.models import Titles, Genre, Category
from .serializers import TitlesSerializer, CategorySerializer, GenreSerializer
from .permissions import AdminOrReadOnly


class TitleViewSet(viewsets.ModelViewSet):

    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (AdminOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
