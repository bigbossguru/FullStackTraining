from rest_framework.generics import ListCreateAPIView, RetrieveAPIView, ListAPIView, GenericAPIView
from rest_framework.views import Response, status
from drf_yasg.utils import swagger_auto_schema

from .models import Author, Item
from .serializers import AuthorSerializer, ItemSerializer, GetAuthorSerializer, PostItemSerializer


class AuthorView(ListCreateAPIView):
    queryset = Author.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return GetAuthorSerializer
        return AuthorSerializer


class OneAuthorView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = GetAuthorSerializer


class ItemView(ListAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AuthorItemView(GenericAPIView):
    queryset = Item.objects.all()
    serializer_class = PostItemSerializer

    @swagger_auto_schema(responses={200: ItemSerializer()})
    def post(self, request, pk):
        serializer = PostItemSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            item = Item(**serializer.validated_data)
            author = Author.objects.get(id=pk)
            item.owner = author
            item.save()
            response_data = serializer.validated_data.copy()
            response_data.update({"owner": pk, "id": item.id})
            return Response(data=response_data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
