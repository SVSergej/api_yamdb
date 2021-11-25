from rest_framework import serializers
from rest_framework_simplejwt.tokens import AccessToken
from rest_framework import status

from api.exceptions import CustomValidator

from users.models import User


class TokenSerializer(serializers.ModelSerializer):
    username = serializers.SlugField(required=True)

    class Meta:
        model = User
        fields = ['username', 'confirmation_code']

    @classmethod
    def get_token(cls, user):
        token = AccessToken.for_user(user)
        return token

    def validate_username(self, value):
        if not User.objects.filter(username=value).exists():
            raise CustomValidator('Нет такого юзера', 'username', status_code=status.HTTP_404_NOT_FOUND)
        return value
