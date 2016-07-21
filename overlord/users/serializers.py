from overlord.users.models import User
from overlord.minions.models import Minion
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    minions = serializers.PrimaryKeyRelatedField(many=True, queryset=Minion.objects.all())

    class Meta:
        model = User
        fields = ('username', 'name', 'minions')
