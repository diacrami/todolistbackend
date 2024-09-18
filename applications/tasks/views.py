from django.shortcuts import render
from rest_framework import viewsets
from .models import Tasks
from .serializer import TasksSerializer, TasksCreateSerializer, TasksUpdateSerializer
# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response

from .managers import TasksManager

from rest_framework.generics import (
    CreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveAPIView
)

class TasksListView(APIView):
    def get(self, request):
        task = Tasks.objects.getActiveTasks()
        serializer = TasksSerializer(task, many=True)
        return Response(serializer.data)

class TaskFilterView(APIView):
    def get(self, request, tasks=None):
        if(tasks=='C' or tasks=='T'):
            tasks = Tasks.objects.filterTasks(tasks)
        else:
            tasks = Tasks.objects.getActiveTasks()
        serializer = TasksSerializer(tasks, many = True)
        return Response(serializer.data)

class TasksCreateView(CreateAPIView):
    serializer_class = TasksCreateSerializer

class TasksUpdateView(RetrieveUpdateAPIView):
    serializer_class = TasksUpdateSerializer
    queryset = Tasks.objects.all()

class TasksDetailView(RetrieveAPIView):
    serializer_class = TasksSerializer
    queryset = Tasks.objects.all()