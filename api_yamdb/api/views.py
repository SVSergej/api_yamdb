from rest_framework import filters, generics, mixins, serializers, viewsets
from reviews.models import Titles, Genre, Category
from .serializers import TitlesSerializer, CategorySerializer, GenreSerializer, InputSerializer, OutputSerializer, RegistrationSerializer, TokenSerializer
from .permissions import AdminOrReadOnly
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from users.models import User
from rest_framework_simplejwt.views import TokenObtainPairView
from django.core.mail import send_mail
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from rest_framework_simplejwt.tokens import AccessToken
from django.contrib.auth.models import update_last_login


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer


class GenreViewSet(viewsets.ModelViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    queryset = Genre.objects.all()
    pagination_class = LimitOffsetPagination
    serializer_class = GenreSerializer


class RegistrationView(APIView):
    permission_classes = (AllowAny,)
    serializer_class = RegistrationSerializer
    
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data=user)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        confirmation_code = "asdasdasdasd"
        send_mail(
            subject='Ваш код подтверждения YaMDb',
            message=f'Код подтверждения:{confirmation_code}',
            from_email=settings.EMAIL_HOST_USER,
            recipient_list='Zayan_93@mail.ru'
         )

        return Response(serializer.data, status=status.HTTP_201_CREATED)

# default_token_generator.make_token(user)

class CustomJWTTokenView(generics.CreateAPIView):
    serializer_class = TokenSerializer
    permission_classes = (AllowAny,)

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.get(username=request.data['username'])
        token = AccessToken.for_user(user)
        return Response({'Token': str(token)}, status.HTTP_200_OK)
