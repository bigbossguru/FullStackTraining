from rest_framework.serializers import ModelSerializer

from .models import Author, Item


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["id", "title", "description", "owner"]


class AuthorItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["title", "description"]


class PostItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = ["title", "description"]


class AuthorSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = ["email", "hashed_password"]


class GetAuthorSerializer(ModelSerializer):
    items = AuthorItemSerializer(many=True)

    class Meta:
        model = Author
        fields = ["id", "email", "is_active", "items"]
