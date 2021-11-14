from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from djoser.views import TokenCreateView
from api.views import RegistrationView, CustomJWTTokenView
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
# <<<<<<< HEAD
#     path('api/v1/users/', RegistrationView.as_view()),
#     path('api/v1/', include('djoser.urls.jwt')),
#     path('api/v1/auth/token', TokenCreateView.as_view()),
#     path('api/v1/auth/signup/', TokenCreateView.as_view()),
#     path('api/v1/auth/token/', CustomJWTTokenView.as_view(), name='token_obtain'),
#     path('api/v1/auth/token/refresh/', CustomJWTTokenView.as_view(), name='token_refresh'),
# =======
# >>>>>>> origin/users
]
