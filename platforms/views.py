# Create your views here.
import json
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import PlatformsSerializer
from .models import Platforms


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/platforms-list/',
        'Detail View': '/platforms-detail/<str:pk>/',
        'Create': '/platforms-create/',
        'Update': '/platforms-update/<str:pk>/',
        'Delete': '/platforms-delete/<str:pk>/',
    }
    return Response(api_urls)


@api_view(['GET'])
def PlatforsmList(request):
    platform = Platforms.objects.all()
    serializer = PlatformsSerializer(platform, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def PlatformsDetail(request, pk):
    platform = Platforms.objects.get(id=pk)
    serializer = PlatformsSerializer(platform, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def PlatformsCreate(request):
    serializer = PlatformsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['PATCH'])
def PlatformsUpdate(request, pk):
    platform = Platforms.objects.get(id=pk)
    serializer = PlatformsSerializer(instance=platform, data=request.data)

    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)


@api_view(['DELETE'])
def PlatformsDelete(request, pk):
    platform = Platforms.objects.get(id=pk)
    platform.delete()

    return Response('Item succsesfully delete!')
