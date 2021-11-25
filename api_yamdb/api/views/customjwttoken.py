from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.tokens import default_token_generator

from users.models import User

from ..serializers.token import TokenSerializer


class CustomJWTTokenView(generics.CreateAPIView):
    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        user = User.objects.get(username=request.data['username'])
        token = AccessToken.for_user(user)
        if default_token_generator.check_token(user, request.data['confirmation_code']) is True:
            return Response({'Token': str(token)}, status.HTTP_200_OK)
        return Response(status=status.HTTP_400_BAD_REQUEST)
