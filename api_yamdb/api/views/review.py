from django.shortcuts import get_object_or_404
from rest_framework import status, viewsets
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response
from reviews.models import Review, Title

from ..permissions import ModeratorOrReadOnly
from ..serializers.review import ReviewSerializer


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (ModeratorOrReadOnly,)
    pagination_class = LimitOffsetPagination

    def _get_title(self):
        return get_object_or_404(Title,
                                 pk=self.kwargs.get('title_id'))

    def get_queryset(self):
        return self._get_title().reviews.all()

    def perform_create(self, serializer):
        serializer.save(author=self.request.user, title=self._get_title())

    def delete(self, request, pk):
        if request.user.is_admin or request.user.is_moderator:
            snippet = super().get_queryset().id
            snippet.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_403_FORBIDDEN)
