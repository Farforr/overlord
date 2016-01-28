# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

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


    # URL pattern for the NetworkUpdateView
    url(
        regex=r'^~update/$',
        view=views.NetworkUpdateView.as_view(),
        name='update'
    ),

    # URL pattern for the NetworkCreateView
    url(
        regex=r'^~create/$',
        view=views.NetworkCreateView.as_view(),
        name='create'
    ),

    # Api URL patterns
    url(
        regex=r"^api/$",
        view=views.NetworkList.as_view(),
        name="network_rest_api"
    ),

    url(
        regex=r"^api/(?P<pk>[0-9]+)/$",
        view=views.NetworkDetail.as_view(),
        name="network_rest_api"
    ),

    # URL pattern for the NetworkDetailView
    url(
        regex=r'^(?P<name>[\w]+)/$',
        view=views.NetworkDetailView.as_view(),
        name='detail'
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
