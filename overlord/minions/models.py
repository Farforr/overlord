from overlord.core.models import DatedModel, NamedModel
# from django.core.validators import ValidationError
from django.core.urlresolvers import reverse
from django.db import models
from overlord.users.models import User


class Minion(DatedModel, NamedModel):
    owner = models.ForeignKey(User, related_name='minions')
    parent = models.ForeignKey(
        'self',
        related_name='minions',
        blank=True,
        null=True
    )

    def get_absolute_url(self):
        return reverse("minions:minion-detail", kwargs={"name": self.name})

    def is_top_level(self):
        return self.parent is None


class MinionData(DatedModel):
    minion = models.ForeignKey(Minion, related_name='data')
    field_name = models.CharField(max_length=80)
    field_value = models.CharField(max_length=80)

    def get_absolute_url(self):
        return reverse("minions:data-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return self.field_name + ' : ' + self.field_value
