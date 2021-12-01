from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    class Meta:
        model = User
        fields = (
            'email', 'username',
            'bio', 'role',
            'first_name', 'last_name',
        )
