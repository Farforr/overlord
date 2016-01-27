from django.db import models
from overlord.core.models import DatedModel, NamedModel
from overlord.nodes.models import Node


class SensorType(DatedModel, NamedModel):
    manufacturer = models.CharField(max_length=45)
    units = models.CharField(max_length=10)


class Sensor(DatedModel, NamedModel):
    node = models.ForeignKey(Node)
    model = models.ForeignKey(SensorType)


class SensorData(DatedModel):
    value = models.IntegerField()
    sensor = models.ForeignKey(Sensor)
