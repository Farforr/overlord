from overlord.users.models import User
from overlord.networks.models import Network
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    networks = serializers.PrimaryKeyRelatedField(many=True, queryset=Network.objects.all())

    class Meta:
        model = User
        fields = ('username', 'name', 'networks')
