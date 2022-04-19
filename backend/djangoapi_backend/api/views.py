from rest_framework.generics import ListCreateAPIView

from .models import Author, Item
from .serializers import AuthorSerializer, ItemSerializer


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
