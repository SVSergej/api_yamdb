from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser

from ..serializers.review import ReviewSerializer
from ..permissions import ModeratorOrReadOnly, IsAdminPermission
from reviews.models import Review, Titles


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (ModeratorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def get_queryset(self):
        title_id = get_object_or_404(
            Titles,
            pk=self.kwargs.get('title_id')
        )
        return Review.objects.filter(title_id=title_id.id)

    def perform_create(self, serializer):
        title = get_object_or_404(
            Titles, pk=self.kwargs['title_id']
        )
        serializer.save(title=title)
