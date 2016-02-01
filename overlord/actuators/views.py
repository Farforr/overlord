# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Actuator, ActuatorData
from .serializers import ActuatorSerializer, ActuatorDataSerializer
from overlord.core.permissions import IsOwnerOrReadOnly


class ActuatorDetailView(LoginRequiredMixin, DetailView):
    model = Actuator
    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"


class ActuatorRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("actuators:detail",
                       kwargs={"name": self.request.actuator.name})


class ActuatorUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    model = Actuator

    # send the user back to the actuator page after a successful update
    def get_success_url(self):
        return reverse("actuators:detail",
                       kwargs={"name": self.request.actuator.name})


class ActuatorListView(LoginRequiredMixin, ListView):
    model = Actuator
    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"


# Api Views
class ActuatorList(ListCreateAPIView):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()


class ActuatorDetail(RetrieveUpdateDestroyAPIView):
    queryset = Actuator.objects.all()
    serializer_class = ActuatorSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class ActuatorDataList(ListCreateAPIView):
    queryset = ActuatorData.objects.all()
    serializer_class = ActuatorDataSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()
