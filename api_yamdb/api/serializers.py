from rest_framework import serializers
from reviews.models import Categories, Genres, Titles, Genre_Title
from users.models import User
import datetime as dt
from django.core.mail import send_mail


class CategoriesSerializer(serializers.ModelSerializer):
    titles = serializers.StringRelatedField(read_only=True, many=True)

    class Meta:

        model = Categories
        fields = ('id','name','slug','titles')


class GenresSerializer(serializers.ModelSerializer):
    titles = serializers.StringRelatedField(read_only=True, many=True)
    class Meta:

        model = Genres
        fields = ('id','name', 'slug', 'titles')


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True)

    class Meta:

        model = Titles
        fields = ('id', 'name', 'year', 'genre', 'category')
    
    def create(self, validated_data):

        genres = validated_data.pop('genre')
        title = Titles.objects.create(**validated_data)

        for genre in genres:

            current_genre, status = Genres.objects.get_or_create(
                **genre)

            Genre_Title.objects.create(
                genre=current_genre, title=title)
        return title
    
    def validate_year(self, value):
        year = dt.date.today().year
        if value > year:
            raise serializers.ValidationError('Проверьте год!')
        return value

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):

        user = User.objects.create_user(
            username=validated_data['username'],
            password=validated_data['password'],
        )

        return user

    class Meta:
        model = User
        # Tuple of serialized model fields (see link [2])
        fields = ( "id", "username", "password", )
