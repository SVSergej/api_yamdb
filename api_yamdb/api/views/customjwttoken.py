from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.tokens import AccessToken

from users.models import User

from api.serializers.token import TokenSerializer


class CustomJWTTokenView(generics.CreateAPIView):
    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=request.data['username'])
        token = AccessToken.for_user(user)
        return Response({'Token': str(token)}, status.HTTP_200_OK)
