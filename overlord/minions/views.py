# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.core.urlresolvers import reverse
from django.contrib import messages
from django.views.generic import DetailView, ListView, RedirectView, UpdateView, CreateView


from rest_framework.generics import ListCreateAPIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework import permissions


from braces.views import LoginRequiredMixin

from .models import Minion, MinionRequest, MinionRequestHeader, MinionRequestBody, MinionData
# from .serializers import NetworkSerializer
from overlord.core.permissions import IsOwnerOrReadOnly


# class MinionActionMixin(object):
#     fields = ['name']

#     @property
#     def success_msg(self):
#         return NotImplemented

#     def form_valid(self, form):
#         messages.info(self.request, self.success_msg)
#         return super(MinionActionMixin, self).form_valid(form)

class MinionListView(LoginRequiredMixin, ListView):
    model = Minion
    def get_context_data(self, **kwargs):
        context = super(MinionListView, self).get_context_data(**kwargs)
        return context

    # These next two lines tell the view to index lookups by username
    slug_field = "name"
    slug_url_kwarg = "name"

class MinionCreateView(LoginRequiredMixin, CreateView):
    model = Minion
    success_msg = 'Minion Created!'
    template_name_suffix = '_create_form'
    fields = ['name', 'parent']

    def form_valid(self, form):
        owner = self.request.user
        form.instance.owner = owner
        return super(MinionCreateView, self).form_valid(form)


class MinionDetailView(LoginRequiredMixin, DetailView):
    model = Minion

    # These next two lines tell the view to index lookups by name
    slug_field = "name"
    slug_url_kwarg = "name"

    def get_context_data(self, **kwargs):
        context = super(MinionDetailView, self).get_context_data(**kwargs)
        context["minion_list"] = Minion.objects.filter(parent=self.object.pk)
        context["data_list"] = MinionData.objects.filter(minion=self.object.pk)
        return context

class MinionDataDetailView(LoginRequiredMixin, DetailView):
    slug_field = "pk"
    slug_url_kwarg = "pk"
    model = MinionData

class MinionRequestDetailView(LoginRequiredMixin, DetailView):
    slug_field = "pk"
    slug_url_kwarg = "pk"
    model = MinionRequest

    def get_context_data(self, **kwargs):
        context = super(MinionRequestDetailView, self).get_context_data(**kwargs)
        context["headers"] = MinionRequestHeader.objects.filter(request=self.object.pk)
        context["body"] = MinionRequestBody.objects.filter(request=self.object.pk)
        return context



# class MinionRedirectView(LoginRequiredMixin, RedirectView):
#     permanent = False

#     def get_redirect_url(self):
#         return reverse("minions:detail",
#                        kwargs={"name": self.request.minion.name})


# class MinionUpdateView(LoginRequiredMixin, MinionActionMixin, UpdateView):

#     fields = ['name']
#     success_msg = 'Minion Updated!'

#     model = Minion

#     # send the user back to the network page after a successful update
#     def get_success_url(self):
#         return reverse("minions:detail",
#                        kwargs={"name": self.request.minion.name})




# # Api Views
# class NetworkList(ListCreateAPIView):
#     queryset = Network.objects.all()
#     serializer_class = NetworkSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)

#     def perform_create(self, serializer):
#         serializer.save(owner=self.request.user)


# class NetworkDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Network.objects.all()
#     serializer_class = NetworkSerializer
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)
