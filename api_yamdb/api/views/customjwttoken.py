from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers

from users.models import User

from ..serializers.token import TokenSerializer


class CustomJWTTokenView(generics.CreateAPIView):
    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        username = request.data.get('username', None)
        email = request.data.get('email', None)
        user = User.objects.get(username=username)
        token = AccessToken.for_user(user)

        user_valid = True

        if User.objects.filter(username=username, email=email):
            user_valid = False
            raise serializers.ValidationError('Ошибка хз2')
        elif User.objects.filter(username=username):
            raise serializers.ValidationError('Пользователь с таким имнем существует')
        elif User.objects.filter(email=email):
            raise serializers.ValidationError('Эта почта используется другим пользователем')

        if user_valid:
            if default_token_generator.check_token(user, request.data['confirmation_code']) is True:
                return Response({'Token': str(token)}, status.HTTP_200_OK)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        raise serializers.ValidationError ('Ошибка хз')
