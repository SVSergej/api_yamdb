from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from users.models import User


class TokenSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']

    @classmethod
    def get_token(cls, user):
        token = AccessToken.for_user(user)
        return token
