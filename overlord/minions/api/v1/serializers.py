from rest_framework import serializers
from ... models import Minion, MinionData



class MinionDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = MinionData

class MinionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Minion

    data = MinionDataSerializer(many=True)