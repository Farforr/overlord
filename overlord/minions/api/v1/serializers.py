from rest_framework import serializers
from ...models import Minion, MinionData


class MinionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Minion
        fields = ('pk', 'name', 'last_modified', 'data', 'url')
        extra_kwargs = {'url': {'view_name': 'minions:api:minion-detail'}}

    data = serializers.HyperlinkedRelatedField(
        many=True,
        view_name='minions:api:data-detail',
        read_only=True,
        lookup_field='pk'
    )


class MinionDataSerializer(serializers.HyperlinkedModelSerializer):
    minion = serializers.HyperlinkedRelatedField(
        view_name='minions:api:minion-detail',
        read_only=True,
        lookup_field='pk'
    )

    class Meta:
        model = MinionData
        fields = ('minion', 'url', 'field_name',
                  'field_value', 'last_modified')
        extra_kwargs = {'url': {'view_name': 'minions:api:data-detail'}}
