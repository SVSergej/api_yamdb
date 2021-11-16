from django.db import models
from users.models import User
from rest_framework.validators import UniqueValidator


class Category(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=256)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.slug


# class GenreTitle(models.Model):
class Genre_Title(models.Model):
    genre = models.ForeignKey(Genre, on_delete=models.CASCADE)
    title = models.ForeignKey("Titles", on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.genre} {self.title}'


class Titles(models.Model):
    name = models.CharField(max_length=200)
    year = models.PositiveSmallIntegerField()
    description = models.CharField(max_length=200)
    genre = models.ManyToManyField(
        Genre,
        through="Genre_Title",
        related_name='titles'
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        null=True,
        related_name='titles'
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='titles_reviews',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authors_reviews',
    )
    score = models.PositiveSmallIntegerField()
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.text


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='reviews_comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='authors_comments'
    )
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.text
