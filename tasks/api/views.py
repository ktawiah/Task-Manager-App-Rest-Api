from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import TaskSerializer
from tasks.models import Task


class TasksViewSet(ModelViewSet):
    serializer_class = TaskSerializer
    queryset = Task.objects.all()
    http_method_names = [
        "get",
        "post",
        "put",
        "patch",
        "delete",
    ]
    permission_classes = [IsAuthenticated]
