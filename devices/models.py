from django.db import models
from core.models import DatedModel, NamedModel
from networks.models import Network

class Node(DatedModel, NamedModel):
    network = models.ForeignKey(Network)


class SensorType(DatedModel, NamedModel):
    manufacturer = models.CharField(max_length=45)
    units = models.CharField(max_length=10)


class Sensor(DatedModel, NamedModel):
    node = models.ForeignKey(Node)
    model = models.ForeignKey(SensorType)


class ActuatorType(DatedModel, NamedModel):
    manufacturer = models.CharField(max_length=45)


class Actuator(DatedModel, NamedModel):
    node = models.ForeignKey(Node)
    model = models.ForeignKey(ActuatorType)


class SensorData(DatedModel):
    value = models.IntegerField()
    sensor = models.ForeignKey(Sensor)


class ActuatorData(DatedModel):
    value = models.IntegerField()
    actuator = models.ForeignKey(Actuator)
