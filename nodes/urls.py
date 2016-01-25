# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the NodeListView
    url(
        regex=r'^$',
        view=views.NodeListView.as_view(),
        name='list'
    ),

    # URL pattern for the NodeRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.NodeRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the NodeDetailView
    url(
        regex=r'^(?P<name>[\w]+)/$',
        view=views.NodeDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the NodeUpdateView
    url(
        regex=r'^~update/$',
        view=views.NodeUpdateView.as_view(),
        name='update'
    ),
]
