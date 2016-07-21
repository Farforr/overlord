# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import include, url

from . import views

urlpatterns = [

    # URL pattern for the MinionListView
    url(
        regex=r'^$',
        view=views.MinionListView.as_view(),
        name='minion-list'
    ),

    # URL pattern for the MinionCreateView
    url(
        regex=r'^~create/$',
        view=views.MinionCreateView.as_view(),
        name='minion-create'
    ),

    # URL pattern for the MinionDetailView
    url(
        regex=r'^minion/(?P<name>[\w]+)/$',
        view=views.MinionDetailView.as_view(),
        name='minion-detail'
    ),

    # URL pattern for the MinionDataDetailView
    url(
        regex=r'^data/(?P<pk>[0-9]+)/$',
        view=views.MinionDataDetailView.as_view(),
        name='data-detail'
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

    url(r'^api/v1/', include("overlord.minions.api.v1.urls", namespace="api")),
]


