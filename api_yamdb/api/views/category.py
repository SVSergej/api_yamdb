from rest_framework import viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework import filters

from reviews.models import Category
from ..serializers.category import CategorySerializer
from ..permissions import AdminOrReadOnly


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


