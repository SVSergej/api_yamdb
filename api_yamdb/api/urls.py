from django.urls import include, path
from rest_framework.routers import DefaultRouter
from api.views import TitleViewSet, CategoryViewSet, GenreViewSet

router_v1 = DefaultRouter()
router_v2 = DefaultRouter()

 

router_v1.register('titles', TitleViewSet, basename='titles')
router_v1.register('genres', GenreViewSet, basename='genres')
router_v1.register('categories', CategoryViewSet, basename='categories')

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]