from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination

from api_yamdb.reviews.models import Category
from ..serializers.category import CategorySerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = CategorySerializer
