from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.pagination import LimitOffsetPagination
from django.shortcuts import get_object_or_404

from users.models import User

from api.serializers.user import UserSerializer
from api.permissions import IsAdminPermission


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = 'username'
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = LimitOffsetPagination
    permission_classes = (IsAdminPermission,)


class UserApi(APIView):
    permission_classes = (IsAdminPermission,)
    serializer_class = UserSerializer
    queryset = User.objects.all()

    def get(self, request):
        user = get_object_or_404(User, user=request.user)
        serializer = self.serializer_class(user)
        return Response(serializer.data)

    def patch(self, request):
        serializer = self.serializer_class(
            request.user, data=request.data, partial=True, context={'request': request}
        )
        if serializer.is_valid():
            serializers.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
