from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TasksViewSet

router = SimpleRouter()

router.register(viewset=TasksViewSet, prefix="", basename="")

urlpatterns = [
    path("", include(router.urls)),
]
