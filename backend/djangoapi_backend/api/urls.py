from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from .views import RegisterView

urlpatterns = [
    path("auth/login/", TokenObtainPairView.as_view(), name="login"),
    path("auth/register/", RegisterView.as_view(), name="register"),
    path("auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
