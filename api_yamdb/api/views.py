from rest_framework import filters, mixins, permissions, viewsets 
from reviews.models import Titles, Genres, Categories
from .serializers import TitlesSerializer, CategoriesSerializer, GenresSerializer, UserSerializer
from .permissions import AdminOrReadOnly
from users.models import User
from rest_framework.generics import CreateAPIView


class TitleViewSet(viewsets.ModelViewSet):

    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (AdminOrReadOnly,)


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class GenreViewSet(viewsets.ModelViewSet):

    queryset = Genres.objects.all()
    serializer_class = GenresSerializer

class CreateUserView(CreateAPIView):

    model = User
    permission_classes = [
        AdminOrReadOnly,
    ]
    serializer_class = UserSerializer
