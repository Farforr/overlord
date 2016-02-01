from rest_framework import serializers
from .models import Sensor, SensorData, SensorType


class SensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sensor
        fields = ('name', 'created', 'last_modified', 'node', 'model')


class SensorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorData
        fields = ('created', 'last_modified', 'sensor', 'value')


class SensorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SensorType
        fields = ('name', 'created', 'last_modified', 'manufacturer', 'units')
