# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from .models import *


def index(request):
    tweets = Tweet.objects.order_by('-publish_date')
    context = {'tweets': tweets}
    return render(request, 'food/index.html', context)


def cart(request):
    orders = Order.objects.all()
    total = sum([o.number * o.price.value for o in orders])
    user = orders[0].user.name
    context = {'user': user, 'orders': orders, 'total': total}
    return render(request, 'food/cart.html', context)

def found(request):
    return render(request, 'food/found.html')

def discuss(request):
    return render(request, 'food/discuss.html')

def forward(request):
    return render(request, 'food/forward.html')

def tweet_detail(request, tweet_id):
    tweet = get_object_or_404(Tweet, pk=tweet_id)
    return render(request, 'food/tweet.html', {'tweet': tweet})


def tweet_buy(request, tweet_id):
    user = int(request.POST['user'])
    number = int(request.POST['number'])
    price = int(request.POST['price'])
    o = Order(user=User.objects.get(pk=user), price=Price.objects.get(pk=price), number=number)
    o.save()
    return HttpResponseRedirect(reverse('food:cart'))

