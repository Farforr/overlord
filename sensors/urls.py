# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    # URL pattern for the SensorListView
    url(
        regex=r'^$',
        view=views.SensorListView.as_view(),
        name='list'
    ),

    # URL pattern for the SensorRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.SensorRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the SensorDetailView
    url(
        regex=r'^(?P<name>[\w]+)/$',
        view=views.SensorDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the SensorUpdateView
    url(
        regex=r'^~update/$',
        view=views.SensorUpdateView.as_view(),
        name='update'
    ),
]
