from rest_framework import serializers
from reviews.models import Category, Genre, Titles, Genre_Title
from users.models import User
import datetime as dt
from django.contrib.auth.tokens import default_token_generator
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import AccessToken

class CategorySerializer(serializers.ModelSerializer):


    class Meta:
        model = Category
        fields = ('name','slug')


class GenreSerializer(serializers.ModelSerializer):


    class Meta:
        model = Genre
        fields = ('name', 'slug')


class OutputSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        many=True,
        slug_field='slug',
        queryset=Genre.objects.all()
    )
    category = serializers.SlugRelatedField(
        slug_field='slug',
        queryset=Category.objects.all()
    )


    class Meta:
        model = Titles
        fields = ('name', 'year', 'genre', 'category')


class InputSerializer(serializers.Serializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    name = serializers.StringRelatedField(read_only=True)
    year = serializers.IntegerField(read_only=True)


    class Meta:
        fields = ('name', 'year', 'genre', 'category')


class TitlesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Titles
        fields = ('id', 'name', 'year', 'genre', 'category')

    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год!')
        return value


class RegistrationSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['email', 'username']

    def create(self, validated_data):

        return User.objects.create_user(**validated_data)


class TokenSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['token',]


# class TokenSerializer(serializers.ModelSerializer):

    @classmethod
    def get_token(cls, user):
        token = AccessToken.for_user(user)
        return token

