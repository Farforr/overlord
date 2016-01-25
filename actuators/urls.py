# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the ActuatorListView
    url(
        regex=r'^$',
        view=views.ActuatorListView.as_view(),
        name='list'
    ),

    # URL pattern for the ActuatorRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.ActuatorRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the ActuatorDetailView
    url(
        regex=r'^(?P<name>[\w]+)/$',
        view=views.ActuatorDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the ActuatorUpdateView
    url(
        regex=r'^~update/$',
        view=views.ActuatorUpdateView.as_view(),
        name='update'
    ),
]
