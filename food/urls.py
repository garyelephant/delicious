# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^tweet/(?P<pk>[0-9]+)/$', views.TweetDetailView.as_view(), name='tweet_detail'),
    url(r'^tweet/(?P<tweet_id>[0-9]+)/buy/$', views.tweet_buy, name='tweet_buy'),
    url(r'^tweet/(?P<pk>[0-9]+)/discuss/$', views.DiscussView.as_view(), name='discuss'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^found/$', views.found, name='found'),
]
