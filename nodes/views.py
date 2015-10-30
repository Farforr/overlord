# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from .models import Node
from sensors.models import Sensor
from actuators.models import Actuator


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
