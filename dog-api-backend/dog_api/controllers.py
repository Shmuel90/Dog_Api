from django.shortcuts import render
from django.core import serializers
from django.http import HttpResponse

# Django REST Framework
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import parsers, renderers
from rest_framework import status

# API
from dog_api.models import *

def home(request):
	# Send requests for '/' to the Ember.js app
	return render(request, 'index.html')

class DogDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )
    
    def get(self, request, pk, *args, **kwargs):
        dog = Dog.objects.filter(pk=pk)
        json_data = serializers.serialize('json', dog)
        content = {'dog': json_data}
        return HttpResponse(json_data, content_type='json')

    def put(self, request, pk, *args, **kwargs):
        dog = Dog.objects.get(pk=pk)
        if request.data.get('name'):
            dog.name = request.data.get('name')
        if request.data.get('age'):
            dog.age = int(request.data.get('age'))
        if request.data.get('color'):
            dog.color = request.data.get('color')
        if request.data.get('favoriteFood'):
            dog.favoritefood = request.data.get('favoriteFood')
        if request.data.get('favoriteToy'):
            dog.favoritetoy = request.data.get('favoriteToy')
        if request.data.get('gender'):
            dog.gender = request.data.get('gender')
        if request.data.get('breed'):
            if Breed.objects.filter(pk=request.data.get('breed')).exists():
                dog.breed = Breed.objects.get(pk=request.data.get('breed'))
            else:
                return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

        try:
            dog.clean_fields()
        except Exception:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

        dog.save()
        return Response({'success':True}, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        if Dog.objects.filter(pk=pk).exists():
            Dog.objects.get(pk=pk).delete()
            return Response({'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

class DogList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        dog = Dog.objects.all()
        json_data = serializers.serialize('json', dog)
        content = {'dog': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, format=None):
        name = request.data.get('name')
        age = int(request.data.get("age"))
        color = request.data.get("color")
        gender = request.data.get("gender")
        favoriteFood = request.data.get("favoriteFood")
        favoriteToy = request.data.get("favoriteToy")
        breed = int(request.data.get("breed"))
        
        if Breed.objects.filter(pk=breed).exists():
            val = Breed.objects.get(pk=breed)
        else:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        
        new = Dog(
            name=name,
            age=age,
            color=color,
            gender=gender,
            favoriteFood=favoriteFood,
            favoriteToy=favoriteToy,
            breed=val,
            
		)
        try:
            new.clean_fields()
        except Exception:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        
        new.save()
        return Response({'success':True}, status=status.HTTP_200_OK)
                        

class BreedDetail(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )
    
    SIZE_CHOICES = {
        ("Tiny", "Tiny"),
        ("Small", "Small"),
        ("Medium", "Medium"),
        ("Large", "Large"),
    }

    def get(self, request, pk, *args, **kwargs):
        breed = Breed.objects.filter(pk=pk)
        json_data = serializers.serialize('json', breed)
        content = {'breed': json_data}
        return HttpResponse(json_data, content_type='json')

    def put(self, request, pk, *args, **kwargs):
        breed = Breed.objects.get(pk=pk)
        if request.data.get('name'):
            breed.name = request.data.get('name')
        if request.data.get('size'):
            if (any(request.data.get('size') in i for i in SIZE_CHOICES)):
                breed.size = request.data.get('size')
            else:
                return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        if request.data.get('friendliness'):
            breed.friendliness = request.data.get('friendliness')
        if request.data.get('trainability'):
            breed.trainability = request.data.get('trainability')
        if request.data.get('sheddingAmount'):
            breed.sheddingAmount = request.data.get('sheddingAmount')
        if request.data.get('exerciseNeeds'):
            breed.exerciseNeeds = request.data.get('exerciseNeeds')
    
        try:
            breed.clean_fields()
        except Exception:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

        breed.save()
        return Response({'success':True}, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        if Breed.objects.filter(pk=pk).exists():
            Breed.objects.get(pk=pk).delete()
            return Response({'success':True}, status=status.HTTP_200_OK)
        else:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)

class BreedList(APIView):
    permission_classes = (AllowAny,)
    parser_classes = (parsers.JSONParser,parsers.FormParser)
    renderer_classes = (renderers.JSONRenderer, )

    def get(self, request, format=None):
        breed = Breed.objects.all()
        json_data = serializers.serialize('json', breed)
        content = {'breed': json_data}
        return HttpResponse(json_data, content_type='json')

    def post(self, request, format=None):
        name = request.data.get('name')
        size = request.data.get("size")
        friendliness = request.data.get("friendliness")
        trainability = request.data.get("trainability")
        sheddingAmount = request.data.get("sheddingAmount")
        exerciseNeeds = request.data.get("exerciseNeeds")
        
        new = Breed(
            name=name,
            size=size,
            friendliness=friendliness,
            trainability=trainability,
            sheddingAmount=sheddingAmount,
            exerciseNeeds=exerciseNeeds,
        
            
		)
        try:
            new.clean_fields()
        except Exception:
            return Response({'success':False}, status=status.HTTP_400_BAD_REQUEST)
        
        new.save()
        return Response({'success':True}, status=status.HTTP_200_OK)       