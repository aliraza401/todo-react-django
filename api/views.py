from django.shortcuts import render
# from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from .serializers import TaskSerializer
from .models import *

# Create your views here.

@api_view(['GET'])
def ApiInfo(request):

    list_urls = {
        'list' : 'list/',
        'detail':'detail/<int:pk>',
        'create': 'create/',
        'update': 'update/<int:pk>',
        'delete': 'delete/',
    }
    return Response( list_urls )


@api_view(['GET'])
def TaskList(request):
    data = TaskSerializer( Task.objects.all(), many=True )
    return Response(data.data)


@api_view(['GET'])
def TaskDetail(request, id):
    data = TaskSerializer( Task.objects.get(id=id), many=False )
    return Response(data.data)


@api_view(['POST'])
def TaskCreate(request ):
    serializer = TaskSerializer( data =request.data )

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['POST'])
def TaskUpdate(request, id ):
    task = Task.objects.get(id=id)
    serializer = TaskSerializer(data =request.data, instance=task )

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def TaskDelete(request, id ):
    task = Task.objects.get(id=id)
    task.delete()

    return Response('delete success')
