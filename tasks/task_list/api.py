from rest_framework import viewsets
from rest_framework import response

from task_list.serializer import TaskSerializer, TagSerializer
from task_list.models import Task, Tag

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TagView(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
