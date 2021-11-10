from rest_framework import viewsets
from api_yamdb.reviews.models import Categories
from ..serializers.categories import CategoriesSerializer


class CategoryViewSet(viewsets.ModelViewSet):

    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer
