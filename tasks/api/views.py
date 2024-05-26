from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from django.shortcuts import get_object_or_404
from tasks.models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer
from ..pagination import CustomPagination


class TasksViewSet(ViewSet):
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        paginator = CustomPagination()
        instance = paginator.paginate_queryset(queryset, request)
        serializer = TaskSerializer(instance, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(instance)
        return Response(serializer.data, status=HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class SubTasksViewSet(ViewSet):
    def get_queryset(self):
        return SubTask.objects.filter(user=self.request.user)

    def list(self, request):
        queryset = self.get_queryset()
        paginator = CustomPagination()
        instance = paginator.paginate_queryset(queryset=queryset, request=request)
        serializer = SubTaskSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = SubTaskSerializer(instance)
        return Response(serializer.data, status=HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = SubTaskSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        serializer = SubTaskSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = self.get_queryset()
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
