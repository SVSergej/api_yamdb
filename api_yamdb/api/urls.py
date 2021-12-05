from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views.registation import RegistrationView
from .views.customjwttoken import CustomJWTTokenView
from .views.user import UserViewSet

from .views import (
    GenreViewSet,
    TitleViewSet,
    ReviewViewSet,
    CommentViewSet,
    CategoryList,
    CategoryDetail
)


router_v1 = DefaultRouter()

router_v1.register('titles',
                   TitleViewSet,
                   basename='titles')
router_v1.register('genres',
                   GenreViewSet,
                   basename='genres')
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet,
    basename='review'
)
router_v1.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet,
    basename='comment'
)
router_v1.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
    path('v1/categories/', CategoryList.as_view() ),
    path('v1/categories/<slug:slug>/', CategoryDetail.as_view()),
    path('v1/auth/signup/', RegistrationView.as_view()),
    path('v1/auth/token/', CustomJWTTokenView.as_view(), name='token_obtain'),
]
