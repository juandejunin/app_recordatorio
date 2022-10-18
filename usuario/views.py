import json

from django.forms import model_to_dict
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, View, FormView
from usuario.forms import *
# Create your views here.

from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserSerializer

# Create your views here.

@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/user-list/',
		'Detail View':'/user-detail/<str:pk>/',
		'Create':'/user-create/',
		'Update':'/user-update/<str:pk>/',
		'Delete':'/user-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def UserList(request):
	users = User.objects.all()
	serializer = UserSerializer(users, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def UserDetail(request, pk):
	Users = User.objects.get(id=pk)
	serializer = UserSerializer(Users, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def UserCreate(request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PATCH'])
def UserUpdate(request, pk):
	Users = User.objects.get(id=pk)
	serializer = UserSerializer(instance=Users, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def UserDelete(request, pk):
	Users = User.objects.get(id=pk)
	Users.delete()

	return Response('Item succsesfully delete!')



