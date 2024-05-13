from rest_framework.serializers import ModelSerializer
from tasks.models import Task


class TaskSerializer(ModelSerializer):
    class Meta:
        model = Task
        fields = [
            "id",
            "user",
            "title",
            "description",
            "status",
            "priority",
            "deadline",
            "updated_timestamp",
            "created_timestamp",
        ]
