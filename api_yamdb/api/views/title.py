from rest_framework import viewsets
from api_yamdb.reviews.models import Titles
from ..serializers.titles import TitlesSerializer
from ..permissions import AdminOrReadOnly


class TitleViewSet(viewsets.ModelViewSet):

    queryset = Titles.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (AdminOrReadOnly,)
