from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets

from django.shortcuts import get_object_or_404
# from django.core.exceptions import PermissionDenied

from ..serializers.comment import CommentSerializer
from ..permissions import AuthorOrReadOnly
from reviews.models import Review, Comments


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comments.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (AuthorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def _get_review(self):
        review_id = self.kwargs.get('review_id')
        return get_object_or_404(Review, pk=review_id)

    def get_queryset(self):
        review_id = self._get_review().id
        return Comments.objects.filter(review_id=review_id)

    def perform_create(self, serializer):
        review = get_object_or_404(Review, pk=self.kwargs['review_id'])
        serializer.save(author=self.request.user, review=review)
