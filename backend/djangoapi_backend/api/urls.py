from django.urls import path

from .views import AuthorView, OneAuthorView, ItemView, AuthorItemView

urlpatterns = [
    path("users/", AuthorView.as_view(), name="users"),
    path("users/<int:pk>", OneAuthorView.as_view(), name="user"),
    path("users/<int:pk>/item/", AuthorItemView.as_view(), name="user-item"),
    path("items/", ItemView.as_view(), name="items"),
]
