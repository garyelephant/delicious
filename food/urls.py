# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^tweet/(?P<pk>[0-9]+)/$', views.TweetDetailView.as_view(), name='tweet_detail'),
    url(r'^tweet/(?P<tweet_id>[0-9]+)/buy/$', views.tweet_buy, name='tweet_buy'),
    url(r'^tweet/(?P<pk>[0-9]+)/discuss/$', views.DiscussView.as_view(), name='discuss'),
    url(r'^discuss/add/$', views.discuss_add, name='discuss_add'),
    url(r'^cart/$', views.cart, name='cart'),
    url(r'^cart/buy/$', views.cart_buy, name='cart_buy'),
    url(r'^cart/buy/paid/$', views.cart_paid, name='cart_paid'),
    url(r'^order/(?P<pk>[0-9]+)/increase$', views.order_increase, name='order_increase'),
    url(r'^order/(?P<pk>[0-9]+)/decrease$', views.order_decrease, name='order_decrease'),
    url(r'^found/$', views.found, name='found'),
    url(r'^forward/$', views.forward, name='forward'),
]
