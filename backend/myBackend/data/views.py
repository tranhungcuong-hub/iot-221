from rest_framework import generics

from data.serializers import LedSerializer, HumiditySerializer, LightSerializer, TempSerializer
from data.models import Led, humidity, light, temp

class GetLedAPI(generics.ListAPIView):
    serializer_class = LedSerializer

    def get_queryset(self):
        return Led.objects.all()

class PostLedAPI(generics.CreateAPIView):
    serializer_class = LedSerializer

######################################################
class GetHumidityAPI(generics.ListAPIView):
    serializer_class = HumiditySerializer

    def get_queryset(self):
        return humidity.objects.all()

class PostHumidityAPI(generics.CreateAPIView):
    serializer_class = HumiditySerializer

######################################################
class GetTempAPI(generics.ListAPIView):
    serializer_class = LightSerializer

    def get_queryset(self):
        return light.objects.all()

class PostTempAPI(generics.CreateAPIView):
    serializer_class = LightSerializer

######################################################
class GetLightAPI(generics.ListAPIView):
    serializer_class = TempSerializer

    def get_queryset(self):
        return temp.objects.all()

class PostLightAPI(generics.CreateAPIView):
    serializer_class = TempSerializer