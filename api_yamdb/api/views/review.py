from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from django.shortcuts import get_object_or_404

from ..serializers.review import ReviewSerializer
from ..permissions import ModeratorOrReadOnly
from reviews.models import Review, Titles


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (ModeratorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def _get_title(self):
        title_id = self.kwargs.get('title_id')
        return get_object_or_404(Titles, pk=title_id)

    def get_queryset(self):
        title_id = self._get_title().id
        return Review.objects.filter(title_id=title_id)

    def perform_create(self, serializer):
        title = get_object_or_404(Titles, pk=self.kwargs['title_id'])
        serializer.save(title=title)
