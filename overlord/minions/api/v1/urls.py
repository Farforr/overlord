# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns

from . import views


router = DefaultRouter()
router.register(r'minion', views.MinionViewSet, 'minion')
router.register(r'data', views.MinionDataViewSet, 'data')

urlpatterns = [
    url(
        r'^',
        include(router.urls)
    ),
]
