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
        return get_object_or_404(Titles,
                                 pk=self.kwargs['title_id'])

    def get_queryset(self):
        return Review.objects.filter(title_id=self._get_title().id)

    def perform_create(self, serializer):
        title = get_object_or_404(
            Titles, pk=self.kwargs['title_id']
        )
        # serializer.save(author=self.request.user, title=title)
        serializer.save(title=self._get_title())