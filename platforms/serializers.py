from django.contrib import auth
from rest_framework import serializers
from platforms.models import Platforms


# Renderizar la API
class PlatformsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Platforms
        fields = (
            'id',
            'name',
        )
