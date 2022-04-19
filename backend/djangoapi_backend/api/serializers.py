from rest_framework.serializers import ModelSerializer

from .models import Author, Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
