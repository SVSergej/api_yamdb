# from django.shortcuts import render, get_object_or_404
# from rest_framework import viewsets
# from rest_framework.pagination import LimitOffsetPagination
# from ..reviews.models import Users
# from .serializers import UsersSerializer
#
#
# class SignUpViewSet(viewsets.ModelViewSet):
#     queryset = Users.objects.all()
#     serializer_class = UsersSerializer
#
# from serializers import ReviewSerializer, CommentSerializer
# from api_yamdb.reviews.models import Review, Comments, Titles
#
#
# class ReviewViewSet(viewsets.ModelViewSet):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer
#     permission_classes = ()
#     pagination_class = LimitOffsetPagination
#
#     def _get_title(self):
#         title_id = self.kwargs.get('title_id')
#         return get_object_or_404(Titles, pk=title_id)
#
#     def get_queryset(self):
#         title_id = self._get_title().id
#         return Review.objects.filter(title_id=title_id)
#
#     def perform_create(self, serializer):
#         title = get_object_or_404(Titles, pk=self.kwargs['title_id'])
#         serializer.save(title=title)
#
#
# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comments.objects.all()
#     serializer_class = CommentSerializer
#     permission_classes = ()
#     pagination_class = LimitOffsetPagination
#
#     def _get_review(self):
#         review_id = self.kwargs.get('review_id')
#         return get_object_or_404(Review, pk=review_id)
#
#     def get_queryset(self):
#         review_id = self._get_review().id
#         return Comments.objects.filter(review_id=review_id)
#
#     def perform_create(self, serializer):
#         review = get_object_or_404(Review, pk=self.kwargs['review_id'])
#         serializer.save(author=self.request.user, review=review)

# from rest_framework import filters, mixins, permissions, viewsets
# from reviews.models import Titles, Genres, Categories
# from .serializers import TitlesSerializer, CategoriesSerializer, GenresSerializer
#
#
# class TitleViewSet(viewsets.ModelViewSet):
#
#     queryset = Titles.objects.all()
#     serializer_class = TitlesSerializer
#
#
# class CategoryViewSet(viewsets.ModelViewSet):
#
#     queryset = Categories.objects.all()
#     serializer_class = CategoriesSerializer
#
#
# class GenreViewSet(viewsets.ModelViewSet):
#
#     queryset = Genres.objects.all()
#     serializer_class = GenresSerializer