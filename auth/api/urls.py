from django.urls import include, path
from .views import (
    CustomProviderAuthView,
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    LogoutView,
)

urlpatterns = [
    path("", include("djoser.urls")),
    path("jwt/create/", CustomTokenObtainPairView.as_view(), name="jwt_create"),
    path("jwt/refresh/", CustomTokenRefreshView().as_view(), name="jwt_refresh"),
    path("jwt/verify/", CustomTokenVerifyView.as_view(), name="jwt_verify"),
    path(
        "o/<str:provider>/",
        CustomProviderAuthView.as_view(),
    ),
    path("logout/", LogoutView.as_view()),
]
