from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT
from django.shortcuts import get_object_or_404
from tasks.models import Task, SubTask
from .serializers import TaskSerializer, SubTaskSerializer


class TasksViewSet(ViewSet):
    def list(self, request):
        queryset = Task.objects.filter(user=request.user)
        serializer = TaskSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = Task.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(instance)
        return Response(serializer.data, status=HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = Task.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = Task.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = TaskSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = Task.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class SubTasksViewSet(ViewSet):
    def list(self, request):
        queryset = SubTask.objects.filter(user=request.user)
        serializer = SubTaskSerializer(queryset, many=True)
        return Response(serializer.data, status=HTTP_200_OK)

    def create(self, request):
        serializer = SubTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=HTTP_201_CREATED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk=None):
        queryset = SubTask.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = SubTaskSerializer(instance)
        return Response(serializer.data, status=HTTP_200_OK)

    def update(self, request, pk=None):
        queryset = SubTask.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = SubTaskSerializer(instance, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def partial_update(self, request, pk=None):
        queryset = SubTask.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        serializer = SubTaskSerializer(instance, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_200_OK)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk=None):
        queryset = SubTask.objects.filter(user=request.user)
        instance = get_object_or_404(queryset, pk=pk)
        instance.delete()
        return Response(status=HTTP_204_NO_CONTENT)
