from django.db import models


class Categories(models.Model):

    name = models.CharField(max_length=256)
    slug = models.SlugField()

    def __str__(self):

        return self.slug


class Genres(models.Model):

    name = models.CharField(max_length=256)
    slug = models.SlugField()

    def __str__(self):

        return self.slug



class Genre_Title(models.Model):
    genre = models.ForeignKey(Genres, on_delete=models.CASCADE)
    title = models.ForeignKey("Titles", on_delete=models.CASCADE)
    
    def __str__(self):
        return f'{self.genre} {self.title}'

class Titles(models.Model):

    name = models.CharField(max_length=200)
    year = models.IntegerField()
    description = models.CharField(max_length=200)
    genre = models.ManyToManyField(Genres, through="Genre_Title", related_name='titles')
    category = models.ForeignKey(Categories, on_delete=models.SET_NULL, null=True, related_name='titles')

    def __str__(self):

        return self.name



