from django.db import models


class Categories(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):

        return self.name


class Genres(models.Model):

    name = models.CharField(max_length=256)

    def __str__(self):

        return self.name


class Titles(models.Model):

    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=200)
    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True)

    def __str__(self):

        return self.name


#  class GenresTitles(models.Model):
#    genre = models.ForeignKey(Genres, on_delete=models.SET_NULL, null=True)
#    title = models.ForeignKey(Titles, on_delete=models.CASCADE)

#    def __str__(self):
#        return f'{self.genre} {self.title}'

