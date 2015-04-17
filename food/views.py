# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *


def index(request):
    tweets = Tweet.objects.order_by('-publish_date')
    context = {'tweets': tweets}
    return render(request, 'food/index.html', context)


def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'food/tweet.html', {'tweet': tweet})


def tweet_buy(request, tweet_id):
    # todo 添加订单
    return HttpResponseRedirect(reverse('food:index'))

