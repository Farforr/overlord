# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.views.generic import DetailView, ListView, RedirectView, UpdateView

from braces.views import LoginRequiredMixin

from .models import Network


class NetworkDetailView(LoginRequiredMixin, DetailView):
    model = Network
    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"


class NetworkRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("networks:detail",
                       kwargs={"name": self.request.network.name})


class NetworkUpdateView(LoginRequiredMixin, UpdateView):

    fields = ['name', ]

    model = Network

    # send the user back to the network page after a successful update
    def get_success_url(self):
        return reverse("networks:detail",
                       kwargs={"name": self.request.network.name})


class NetworkListView(LoginRequiredMixin, ListView):
    model = Network
    # These next two lines tell the view to index lookups by username
    slug_field = "name"
    slug_url_kwarg = "name"
