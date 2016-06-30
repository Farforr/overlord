# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    # URL pattern for the MinionListView
    url(
        regex=r'^$',
        view=views.MinionListView.as_view(),
        name='list'
    ),

    # # URL pattern for the MinionRedirectView
    # url(
    #     regex=r'^~redirect/$',
    #     view=views.MinionRedirectView.as_view(),
    #     name='redirect'
    # ),


    # # URL pattern for the MinionUpdateView
    # url(
    #     regex=r'^~update/$',
    #     view=views.MinionUpdateView.as_view(),
    #     name='update'
    # ),

    # URL pattern for the MinionCreateView
    url(
        regex=r'^~create/$',
        view=views.MinionCreateView.as_view(),
        name='create'
    ),

    # URL pattern for the MinionDetailView
    url(
        regex=r'^(?P<name>[\w]+)/$',
        view=views.MinionDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the MinionDataDetailView
    url(
        regex=r'^data/(?P<pk>[\w]+)/$',
        view=views.MinionDataDetailView.as_view(),
        name='data_detail'
    ),

    # URL pattern for the MinionDataDetailView
    url(
        regex=r'^request/(?P<pk>[\w]+)/$',
        view=views.MinionRequestDetailView.as_view(),
        name='request_detail'
    ),
]


urlpatterns = format_suffix_patterns(urlpatterns)
