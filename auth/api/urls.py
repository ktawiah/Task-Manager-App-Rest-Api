from django.urls import include, path
from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
)

urlpatterns = [
    path("", include("djoser.urls")),
    path("jwt/create/", CustomTokenObtainPairView.as_view()),
    path("jwt/refresh/", CustomTokenRefreshView().as_view()),
    path("jwt/verify/", CustomTokenVerifyView.as_view()),
    path("o/<str:provider>/", CustomProviderAuthView.as_view()),
]
