from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()

# router_v1.register(
#     r'titles/(?P<title_id>\d+)/reviews',
#     views.ReviewViewSet,
#     basename='review'
# )
# router_v1.register(
#     r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
#     views.CommentViewSet,
#     basename='comment'
# )
# router_v1.register('api/v1/auth/signup', SignUpViewSet)
# router.register('titles', TitleViewSet, basename='titles')
# router.register('genres', GenreViewSet, basename='genres')
# router.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
