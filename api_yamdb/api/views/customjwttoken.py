from rest_framework.permissions import AllowAny
from rest_framework import generics

from api.serializers.token import TokenSerializer


class CustomJWTTokenView(generics.CreateAPIView):
    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)
