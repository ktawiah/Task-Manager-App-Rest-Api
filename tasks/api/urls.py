from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import TasksViewSet, SubTasksViewSet

router = SimpleRouter()

router.register(viewset=TasksViewSet, prefix="", basename="tasks")
router.register(viewset=SubTasksViewSet, prefix="", basename="subtasks")

urlpatterns = [
    path("", include(router.urls)),
]
