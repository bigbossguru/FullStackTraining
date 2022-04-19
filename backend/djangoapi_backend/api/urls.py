from django.urls import path

from .views import AuthorView

urlpatterns = [
    path("users/", AuthorView.as_view(), name="users"),
]
