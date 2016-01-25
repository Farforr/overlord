# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from .models import Sensor


class SensorDetailView(LoginRequiredMixin, DetailView):
    model = Sensor
    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"


class SensorRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("sensors:detail",
                       kwargs={"name": self.request.sensor.name})


class SensorUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    model = Sensor

    # send the user back to the sensor page after a successful update
    def get_success_url(self):
        return reverse("sensors:detail",
                       kwargs={"name": self.request.sensor.name})


class SensorListView(LoginRequiredMixin, ListView):
    model = Sensor
    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"
