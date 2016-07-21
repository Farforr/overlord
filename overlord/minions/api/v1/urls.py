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

    # url(
    #     regex = r'^$',
    #     view  = views.api_root,
    #     name  = 'index'
    # ),
    # url(
    #     regex = r'^minion/$',
    #     view  = views.MinionList.as_view(),
    #     name  = "minion-list"
    # ),
    # url(
    #     regex = r'^minion/(?P<pk>[\w]+)/$',
    #     view  = views.MinionDetail.as_view(),
    #     name  = "minion-detail"
    # ),
    # url(
    #     regex = r'^data/$',
    #     view  = views.MinionDataList.as_view(),
    #     name  = "data-list"
    # ),
    # url(
    #     regex = r'^data/(?P<pk>[0-9]+)/$',
    #     view  = views.MinionDataDetail.as_view(),
    #     name  = "data-detail"
    # ),
]

# urlpatterns = format_suffix_patterns(urlpatterns)
