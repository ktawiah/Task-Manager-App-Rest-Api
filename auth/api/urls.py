from django.urls import path, include, re_path
from .views import (
    CustomTokenObtainPairView,
    CustomTokenRefreshView,
    CustomTokenVerifyView,
    CustomProviderAuthView,
)

urlpatterns = [
    path("", include("djoser.urls")),
    path("jwt/create/", CustomTokenObtainPairView.as_view()),
    path("jwt/refresh/", CustomTokenRefreshView().as_view()),
    path("jwt/verify/", CustomTokenVerifyView.as_view()),
    # path("o/{{ provider }}/", CustomProviderAuthView.as_view()),
    re_path(
        r"^o/(?P<provider>\S+)/$",
        CustomProviderAuthView.as_view(),
        name="provider-auth",
    ),
]
