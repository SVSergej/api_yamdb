from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router_v1 = DefaultRouter()
# router_v1.register('api/v1/auth/signup', SignUpViewSet)


urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
