from rest_framework import serializers
from .models import Network


class NetworkSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Network
        fields = ('name', 'created', 'last_modified', 'owner')
