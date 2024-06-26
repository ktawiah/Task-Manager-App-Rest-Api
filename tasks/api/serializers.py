from rest_framework.serializers import ModelSerializer
from tasks.models import Task, SubTask


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = "__all__"


class SubTaskSerializer(ModelSerializer):
    class Meta:
        model = SubTask
        fields = "__all__"
