# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import viewsets, permissions
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from overlord.core.permissions import IsOwnerOrReadOnly

from ... models import Minion, MinionData
from . serializers import MinionSerializer, MinionDataSerializer


class MinionViewSet(viewsets.ModelViewSet):
    serializer_class = MinionSerializer
    queryset = Minion.objects.all()
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
    )

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class MinionDataViewSet(viewsets.ModelViewSet):
    serializer_class = MinionDataSerializer
    queryset = MinionData.objects.all()
    permission_classes = (
        # permissions.IsAuthenticatedOrReadOnly,
        # IsOwnerOrReadOnly
    )

    # def perform_create(self, serializer):
    #     serializer.save(minion=Minion.objects.get(pk=14))
