from rest_framework import serializers

from data.models import Led, humidity, temp, light

class LedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Led
        fields = ['id', 'value', 'created_at', 'created_epoch', 'expiration']

class HumiditySerializer(serializers.ModelSerializer):
    class Meta:
        model = humidity
        fields = ['id', 'value', 'created_at', 'created_epoch', 'expiration']

class TempSerializer(serializers.ModelSerializer):
    class Meta:
        model = temp
        fields = ['id', 'value', 'created_at', 'created_epoch', 'expiration']

class LightSerializer(serializers.ModelSerializer):
    class Meta:
        model = light
        fields = ['id', 'value', 'created_at', 'created_epoch', 'expiration']