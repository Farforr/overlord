# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(regex=r'^api/$',
        view=views.UserList.as_view(),
        name='user_rest_api',
    ),

    url(regex=r'^api/(?P<pk>[0-9]+)/$',
        view=views.UserDetail.as_view(),
        name='user_rest_api'
    ),

    # URL pattern for the UserListView
    url(
        regex=r'^$',
        view=views.UserListView.as_view(),
        name='list'
    ),

    # URL pattern for the UserRedirectView
    url(
        regex=r'^~redirect/$',
        view=views.UserRedirectView.as_view(),
        name='redirect'
    ),

    # URL pattern for the UserDetailView
    url(
        regex=r'^(?P<username>[\w.@+-]+)/$',
        view=views.UserDetailView.as_view(),
        name='detail'
    ),

    # URL pattern for the UserUpdateView
    url(
        regex=r'^~update/$',
        view=views.UserUpdateView.as_view(),
        name='update'
    ),
]
