from django.urls import include, re_path, path
from django.views.decorators.csrf import csrf_exempt

from rest_framework import routers
from dog_api.views import *
from dog_api.controllers import *
from dog_api.views import *
router = routers.DefaultRouter(trailing_slash=False)

urlpatterns = [
    re_path(r'^', include(router.urls)),
    path('dogs/', csrf_exempt(DogList.as_view())),
    path('dogs/<int:pk>', csrf_exempt(DogDetail.as_view())),
    path('breeds/', csrf_exempt(BreedList.as_view())),
    path('breeds/<int:pk>', csrf_exempt(BreedDetail.as_view())),
]