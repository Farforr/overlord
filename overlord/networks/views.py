# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView


from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions


from braces.views import LoginRequiredMixin

from .models import Network
from .serializers import NetworkSerializer
from overlord.nodes.models import Node
from overlord.core.permissions import IsOwnerOrReadOnly


class NetworkActionMixin(object):
    fields = ['name']

    @property
    def success_msg(self):
        return NotImplemented

    def form_valid(self, form):
        messages.info(self.request, self.success_msg)
        return super(NetworkActionMixin, self).form_valid(form)


class NetworkCreateView(LoginRequiredMixin, NetworkActionMixin, CreateView):
    model = Network
    success_msg = 'Network Created!'

    def form_valid(self, form):
        owner = self.request.user
        form.instance.owner = owner
        return super(NetworkCreateView, self).form_valid(form)


class NetworkDetailView(LoginRequiredMixin, DetailView):
    model = Network

    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_context_data(self, **kwargs):
        context = super(NetworkDetailView, self).get_context_data(**kwargs)
        context["node_list"] = Node.objects.filter(network__name=self.kwargs['name'])
        return context


class NetworkRedirectView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self):
        return reverse("networks:detail",
                       kwargs={"name": self.request.network.name})


class NetworkUpdateView(LoginRequiredMixin, NetworkActionMixin, UpdateView):

    fields = ['name']
    success_msg = 'Network Updated!'

    model = Network

    # send the user back to the network page after a successful update
    def get_success_url(self):
        return reverse("networks:detail",
                       kwargs={"name": self.request.network.name})


class NetworkListView(LoginRequiredMixin, NetworkActionMixin, ListView):
    model = Network

    def get_context_data(self, **kwargs):
        context = super(NetworkListView, self).get_context_data(**kwargs)
        return context

    # These next two lines tell the view to index lookups by usernameN
    slug_field = "name"
    slug_url_kwarg = "name"


# Api Views
class NetworkList(ListCreateAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class NetworkDetail(RetrieveUpdateDestroyAPIView):
    queryset = Network.objects.all()
    serializer_class = NetworkSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
