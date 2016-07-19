# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.contrib import messages

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from overlord.core.permissions import IsOwnerOrReadOnly

from ... models import Minion, MinionRequest, MinionRequestHeader, MinionRequestBody, MinionData
from . serializers import MinionSerializer


class MinionList(ListCreateAPIView):
    queryset = Minion.objects.defer("data")
    serializer_class = MinionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

class MinionDetail(RetrieveUpdateDestroyAPIView):
    queryset = Minion.objects.all()
    serializer_class = MinionSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
    lookup_field = 'name'



