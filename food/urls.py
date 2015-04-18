# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^found/$', views.found, name='found'),
    url(r'^discuss/$', views.discuss, name='discuss'),
    url(r'^forward/$', views.forward, name='forward'),
    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet_detail, name='tweet_detail'),
    url(r'^tweet/(?P<tweet_id>[0-9]+)/buy/$', views.tweet_buy, name='tweet_buy'),
]
