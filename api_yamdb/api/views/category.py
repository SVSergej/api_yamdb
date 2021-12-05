from rest_framework import viewsets, filters, generics, mixins
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import api_view

from reviews.models import Category
from ..serializers.category import CategorySerializer
from ..permissions import AdminOrReadOnly


class CategoryList(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = CategorySerializer
    permission_classes = (AdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'
    http_method_names = ['delete']
