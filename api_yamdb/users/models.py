from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )

    ROLE_CHOICES = (
        ('U', 'user'),
        ('M', 'moderator'),
        ('A', 'admin'),
    )

    role = models.CharField(
        'Пользовательские роли',
        blank=True,
        max_length=1,
        choices=ROLE_CHOICES,
        default='U'
    )
