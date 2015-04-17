# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet_detail, name='tweet'),
]