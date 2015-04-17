# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    # 首页
    url(r'^$', views.index, name='index'),

    # 微博详情页
    url(r'^tweet/(?P<tweet_id>[0-9]+)/$', views.tweet_detail, name='tweet_detail'),
    url(r'^tweet/(?P<tweet_id>[0-9]+)/buy/$', views.tweet_buy, name='tweet_buy'),


]
