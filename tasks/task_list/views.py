from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from task_list.models import Task, Tag
from task_list.serializers import TaskSerializer, TagSerializer

# Create your views here.
@api_view(['GET','POST'])
@csrf_exempt
def task_list_list(request, format=None):
    if request.method == 'GET':
        task_list = Task.objects.all()
        serializer = TaskSerializer(task_list, many = True)
        return Response(serializer.data)    
    elif request.method == 'POST':
        serializer = TaskSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def task_list_detail(request, pk, format=None):
    try:
        task = Task.objects.get(pk=pk)
    except Task.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TaskSerializer(task)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = TaskSerializer(task, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method =='DELETE':
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET','POST'])
@csrf_exempt
def tag_list(request, format = None):
    if request.method == 'GET':
        tag = Tag.objects.all()
        serializer = TagSerializer(tag, many = True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TagSerializer(data = request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
@csrf_exempt
def tag_detail(request, pk, format = None):
    try:
        tag = Tag.objects.get(pk=pk)
    except Tag.DoesNotExist:
        return Response(status = status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = TagSerializer(tag)
        return Response(serializer.data)
    
    elif request.method =='PUT':
        serializer = TagSerializer(tag, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        tag.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

def index(request):
    return render(request, "task_list/index.html")

def task_full_list(request):
    full_list = Task.objects.all()
    list_dict = {"result_list":full_list}
    return render(request, "task_list/task-list.html",list_dict)

def task_detail(request,pk):
    task_list_verbose = Task.objects.get(pk=pk)
    task_dict = {"result":task_list_verbose}
    return render(request, "task_list/task-detail.html", task_dict)
