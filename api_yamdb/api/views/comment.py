from rest_framework.pagination import LimitOffsetPagination
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from django.shortcuts import get_object_or_404

from ..serializers.comment import CommentSerializer
from ..permissions import ModeratorOrReadOnly
from reviews.models import Review, Comment, User


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (ModeratorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def _get_review(self):
        return get_object_or_404(Review,
                                 pk=self.kwargs.get('review_id'))

    def get_queryset(self):
        return Comment.objects.filter(review_id=self._get_review().id)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, review=self._get_review())

    def delete(self, request, pk):
        if request.user.is_admin or request.user.is_moderator:
            snippet = super().get_queryset().id
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
