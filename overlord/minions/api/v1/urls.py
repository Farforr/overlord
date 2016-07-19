# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view = views.MinionList.as_view(),
        name = "minion_rest_api"
    ),
    url(
        regex=r'^minion/(?P<name>[\w]+)/$',
        view = views.MinionDetail.as_view(),
        name = "minion_rest_api"
    ),
]

urlpatterns = format_suffix_patterns(urlpatterns)
