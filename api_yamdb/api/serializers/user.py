from rest_framework import serializers
from users.models import User


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=True)
    email = serializers.EmailField(required=True)

    def validate_email(self, email):
        if User.objects.filter(email=email):
            raise serializers.ValidationError('Эта почта используется другим пользователем')
        return email

    def validate_username(self, username):
        if User.objects.filter(username=username):
            raise serializers.ValidationError('Эта почта используется другим пользователем')
        return username

    class Meta:
        model = User
        fields = ('email', 'username', 'bio', 'role', 'first_name', 'last_name',)
