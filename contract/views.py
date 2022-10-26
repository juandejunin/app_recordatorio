# Create your views here.
import json

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ContractSerializer, ContractUpdateSerializer
from .models import Contract
from user.models import UserAccount


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List': '/contract-list/',
        'Detail View': '/contract-detail/<str:pk>/',
        'Create': '/contract-create/',
        'Update': '/contract-update/<str:pk>/',
        'Delete': '/contract-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def ContractList(request):
    contract = Contract.objects.all()
    serializer = ContractSerializer(contract, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def ContractDetail(request, pk):
    contract = Contract.objects.get(id=pk)
    serializer = ContractUpdateSerializer(contract, many=False)
    return Response(serializer.data)

@api_view(['POST'])
def ContractCreate(request):
    serializer = ContractUpdateSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['PATCH'])
def ContractUpdate(request, pk):
    contract = Contract.objects.get(id=pk)
    serializer = ContractUpdateSerializer(instance=contract, data=request.data)
    if serializer.is_valid():
        serializer.save()

    return Response(serializer.data)

@api_view(['DELETE'])
def ContractDelete(request, pk):
        contract = Contract.objects.get(id=pk)
        contract.is_active = False
        contract.delete()
        return Response('Item succsesfully delete!')
