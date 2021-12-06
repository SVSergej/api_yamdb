from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
from django.db import models

from users.models import User
import datetime as dt


class Category(models.Model):
    name = models.CharField(max_length=256, verbose_name='category_name')
    slug = models.SlugField(unique=True, verbose_name='category_slug')

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.slug


class Genre(models.Model):
    name = models.CharField(max_length=256, verbose_name='category_name')
    slug = models.SlugField(unique=True, verbose_name='category_slug')

    class Meta:
        verbose_name = 'genre'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.slug


class Genre_Title(models.Model):
    genre = models.ForeignKey(Genre,
                              on_delete=models.CASCADE,
                              verbose_name='genre')
    title = models.ForeignKey("Title",
                              on_delete=models.CASCADE,
                              verbose_name='title')

    def __str__(self):
        return f'{self.genre} {self.title}'

def my_year_validator(value):
    if value > dt.datetime.now().year:
        raise ValidationError(
            _('%(value)s is not a correcrt year!'),
            params={'value': value},
        )
class Title(models.Model):
    name = models.CharField(max_length=200, db_index=True, verbose_name='title_name')
    year = models.PositiveSmallIntegerField(
        validators=[my_year_validator],
        verbose_name="Year"
    )
    description = models.CharField(max_length=200, verbose_name='description')
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

    class Meta:
        verbose_name = 'Title'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Review(models.Model):
    title = models.ForeignKey(
        Title,
        on_delete=models.CASCADE,
        related_name='reviews',
    )
    text = models.TextField(verbose_name='text')
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        related_name='author_review',
    )
    score = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[MinValueValidator(1),
                    MaxValueValidator(10)],
        verbose_name='score'
    )
    pub_date = models.DateField('date published',
                                auto_now_add=True)

    class Meta:
        ordering = ('pub_date',)
        verbose_name = 'отзыв'
        verbose_name_plural = 'review'
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='unique_review'
            )
        ]

    def __str__(self):
        return self.title.name


class Comment(models.Model):
    review = models.ForeignKey(
        Review,
        on_delete=models.CASCADE,
        related_name='comments',
    )
    text = models.TextField()
    author = models.ForeignKey(
        User,
        null=True,
        on_delete=models.CASCADE,
        related_name='authors_comments'
    )
    pub_date = models.DateField('date published',
                                auto_now_add=True)

    class Meta:
        verbose_name = 'comment'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.text
