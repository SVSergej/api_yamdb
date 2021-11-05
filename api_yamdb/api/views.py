from rest_framework import filters, mixins, permissions, viewsets 
from reviews.models import Titles, Genres, Categories
from .serializers import TitlesSerializer, CategoriesSerializer, GenresSerializer


class TitleViewSet(viewsets.ModelViewSet):

    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
