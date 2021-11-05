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
