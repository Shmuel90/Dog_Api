from django.shortcuts import render

# Create your views here.
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt

# Django REST Framework
from rest_framework import viewsets
from rest_framework.response import Response

# API
from dog_api.serializers import *
from dog_api.models import *

class DogViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Dog.objects.all()
    serializer_class = DogSerializer

class BreedViewSet(viewsets.ModelViewSet):
    authentication_classes = []
    queryset = Breed.objects.all()
    serializer_class = BreedSerializer