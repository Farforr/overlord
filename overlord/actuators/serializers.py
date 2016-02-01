from rest_framework import serializers
from .models import Actuator, ActuatorData, ActuatorType


class ActuatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actuator
        fields = ('name', 'created', 'last_modified', 'node', 'model')


class ActuatorDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActuatorData
        fields = ('created', 'last_modified', 'actuator', 'value')


class ActuatorTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActuatorType
        fields = ('name', 'created', 'last_modified', 'manufacturer', 'units')
