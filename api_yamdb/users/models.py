from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
import jwt
from datetime import datetime, timedelta
from django.conf import settings
import uuid


class UserManager(BaseUserManager):
    """
    Django требует, чтобы кастомные пользователи определяли свой собственный
    класс Manager. Унаследовавшись от BaseUserManager, мы получаем много того
    же самого кода, который Django использовал для создания User (для демонстрации).
    """

    def create_user(self, username, email, password=None, role='', bio=''):

        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            role=role, bio=bio
        )
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):

        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.is_staff = True
        user.save()

        return user


class User(AbstractUser):
    bio = models.TextField(
        'Биография',
        blank=True,
    )
    username = models.CharField(db_index=True, max_length=255, unique=True)
    email = models.EmailField(db_index=True, unique=True)
    last_login = models.DateTimeField(auto_now=True)
    confirmation_code = models.CharField(max_length=36, default=uuid.uuid4)
    objects = UserManager()

    def _generate_jwt_token(self):
        """
        Генерирует веб-токен JSON, в котором хранится идентификатор этого
        пользователя, срок действия токена составляет 1 день от создания
        """
        dt = datetime.now() + timedelta(days=1)

        token = jwt.encode({
            'id': self.pk,
            'exp': int(dt.strftime('%s'))
        }, settings.SECRET_KEY, algorithm='HS256')

        return token.decode('utf-8')

    @property
    def token(self):
        return self._generate_jwt_token()

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

    def __str__(self):
        return self.email
