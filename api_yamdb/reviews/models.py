from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    ROLE_CHOICES = (
        ('U', 'user'),
        ('M', 'moderator'),
        ('A', 'admin'),
    )
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    role = models.CharField(
        'Пользовательские роли',
        blank=True,
        max_length=1,
        choices=ROLE_CHOICES,
        default='U'
    )


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


class Review(models.Model):
    title = models.ForeignKey(
        Titles,
        on_delete=models.CASCADE,
        related_name='title_review',
    )
    text = models.TextField()
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='author_review',
    )
    score = models.SmallIntegerField()  # if 1 <= score <= 10
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.text


class Comments(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='review_comment',
    )
    text = models.TextField()
    author = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name='author_comment'
    )
    pub_date = models.DateField('date published', auto_now_add=True)

    def __str__(self):
        return self.text

