# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions

from .models import Node
from .serializers import NodeSerializer
from overlord.core.permissions import IsOwnerOrReadOnly
from overlord.sensors.models import Sensor
from overlord.actuators.models import Actuator


class NodeDetailView(LoginRequiredMixin, DetailView):
    model = Node
    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_context_data(self, **kwargs):
        context = super(NodeDetailView, self).get_context_data(**kwargs)
        context["sensor_list"] = Sensor.objects.filter(node__name=self.kwargs['name'])
        context["actuator_list"] = Actuator.objects.filter(node__name=self.kwargs['name'])
        return context


class NodeRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("nodes:detail",
                       kwargs={"name": self.request.node.name})


class NodeUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    model = Node

    # send the user back to the node page after a successful update
    def get_success_url(self):
        return reverse("nodes:detail",
                       kwargs={"name": self.request.node.name})


class NodeListView(LoginRequiredMixin, ListView):
    model = Node
    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"


# Api Views
class NodeList(ListCreateAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save()


class NodeDetail(RetrieveUpdateDestroyAPIView):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
