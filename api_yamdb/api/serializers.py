# from rest_framework import serializers
# from rest_framework.relations import SlugRelatedField
#
#
# class UsersSerializer(serializers.ModelSerializer):
#     user = SlugRelatedField(slug_field='username', read_only=True)


# class CategoriesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Categories
#         fields = '__all__'
#

# class GenresSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Genres
#         fields = '__all__'
#
#
# class TitlesSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Titles
#         fields = ('id', 'name', 'year', 'genre', 'category')
#
#     def validate_year(self, value):
#         year = dt.date.today().year
#         if value > year:
#             raise serializers.ValidationError('Проверьте год!')
#         return value
#
