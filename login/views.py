from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import NivelSerializer, UserSerializer
# Create your views here.
@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/task-list/',
        'Detail View': 'tastk-detail/<str:pk>/',
        'Create': '/task-create/',
        'Update': '/task-update/<str:pk>/',
        'Delete': '/task-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def userlist(request):
    usuarios = User.objects.all()
    serializer = UserSerializer(usuarios, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def userdetail(request, pk):
    usuarios = User.objects.get(id=pk)
    serializer = UserSerializer(usuarios, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def createuser(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['POST'])
def updateuser(request, pk):
    usuarios = User.objects.get(id=pk)
    serializer = UserSerializer(instance=usuarios, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteuser(request, pk):
    usuarios = User.objects.get(id=pk)
    usuarios.delete()
    return Response('Item succsesfully delete')

def base(request):
    users = User.objects.all()
    return render(request, 'list.html', {'users': users})
