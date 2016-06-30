from overlord.core.models import DatedModel, NamedModel
# from django.core.validators import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from overlord.users.models import User


class Minion(DatedModel, NamedModel):
    owner = models.ForeignKey(User, related_name='minions')
    parent = models.ForeignKey('self', related_name='minions', blank=True, null=True)

    def get_absolute_url(self):
        return reverse("minions:detail", kwargs={"name": self.name})

    def is_top_level(self):
        return self.parent is None

class MinionRequest(DatedModel):
    INCOMING = 'inc'
    OUTGOING = 'out'
    DIRECTIONS = (
        (INCOMING, 'Incoming'),
        (OUTGOING, 'Outgoing'),
    )

    owner = models.ForeignKey(Minion, related_name='requests')
    response = models.BooleanField(default=True)
    direction = models.CharField(choices=DIRECTIONS, max_length=8)

class MinionRequestHeader(DatedModel):
    request = models.ForeignKey(MinionRequest, related_name='headers')
    name = models.CharField(max_length=80)
    value = models.CharField(max_length=80)

class MinionRequestBody(DatedModel):
    request = models.OneToOneField(MinionRequest, related_name='body')
    value = models.TextField()

class MinionData(DatedModel):
    minion = models.ForeignKey(Minion, related_name='data')
    request = models.ForeignKey(MinionRequest, related_name='data')

    field_name = models.CharField(max_length=80)
    field_value = models.CharField(max_length=80)
