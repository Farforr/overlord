# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the NetworkListView
    url(
        regex=r'^$',
        view=views.NetworkListView.as_view(),
        name='list'
    ),

    # URL pattern for the NetworkRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.NetworkRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the NetworkDetailView
    url(
        regex=r'^(?P<name>[\w]+)/$',
        view=views.NetworkDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the NetworkUpdateView
    url(
        regex=r'^~update/$',
        view=views.NetworkUpdateView.as_view(),
        name='update'
    ),
]
