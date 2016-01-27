from django.db import models
from overlord.core.models import DatedModel, NamedModel
from overlord.networks.models import Network


class Node(DatedModel, NamedModel):
    network = models.ForeignKey(Network)
