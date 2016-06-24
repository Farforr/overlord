from overlord.core.models import DatedModel, NamedModel
# from django.core.validators import ValidationError
from django.core.urlresolvers import reverse
from django.db import models


class Underling(DatedModel, NamedModel):
    owner = models.ForeignKey('users.User', related_name='underlings')
    parent = models.ForeignKey('self', related_name='underlings', blank=True)
    top_level = models.BooleanField(default=True)

    def get_absolute_url(self):
        return reverse("underlings:detail", kwargs={"name": self.name})

class UnderlingRequest(DatedModel):
    INCOMING = 'inc'
    OUTGOING = 'out'
    DIRECTIONS = (
        (INCOMING, 'incoming'),
        (OUTGOING, 'outgoing'),
    )

    owner = models.ForeignKey(Underling, related_name='requests')
    response = models.BooleanField(default=True)
    direction = models.CharField(choices=DIRECTIONS, max_length=8)

class UnderlingRequestHeader(models.Model):
    request = models.ForeignKey(UnderlingRequest, related_name='headers')
    name = models.CharField(max_length=80)
    value = models.CharField(max_length=80)

class UnderlingRequestBody(models.Model):
    request = models.OneToOneField(UnderlingRequest, related_name='body')
    value = models.TextField()