from django.db import models
from core.models import DatedModel, NamedModel
from nodes.models import Node


class ActuatorType(DatedModel, NamedModel):
    manufacturer = models.CharField(max_length=45)


class Actuator(DatedModel, NamedModel):
    node = models.ForeignKey(Node)
    model = models.ForeignKey(ActuatorType)


class ActuatorData(DatedModel):
    value = models.IntegerField()
    actuator = models.ForeignKey(Actuator)
