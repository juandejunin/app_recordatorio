from django.contrib import auth
from rest_framework import serializers
from contract.models import Contract
from platforms.models import *
from platforms.serializers import *
from user.serializers import *
from rest_framework.exceptions import AuthenticationFailed


# Esto renderiza la API para que tome forma y obtener los campos de las FK en listado
class ContractSerializer(serializers.ModelSerializer):
    platforms = PlatformsSerializer(read_only=True)
    user = UserCreateSerializer(read_only=True)

    class Meta:
        model = Contract
        fields = '__all__'


# Esto es para Add, Update, Delete
class ContractUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields = '__all__'
