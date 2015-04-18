# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.views import generic
from .models import *


class IndexView(generic.ListView):
    template_name = 'food/index.html'
    context_object_name = 'tweets'

    def get_queryset(self):
        return Tweet.objects.order_by('-publish_date')


def found(request):
    return render(request, 'food/found.html')


def forward(request):
    return render(request, 'food/forward.html')


class TweetDetailView(generic.DetailView):
    model = Tweet
    template_name = 'food/tweet.html'


class DiscussView(generic.DetailView):
    model = Tweet
    template_name = 'food/discuss.html'


def tweet_buy(request, tweet_id):
    user_id = int(request.POST['user'])
    price_ud = int(request.POST['price'])
    number = int(request.POST['number'])

    order = Order.objects.filter(user=User.objects.get(pk=user_id), price=Price.objects.get(pk=price_ud)).all()
    if order:
        order = order[0]
        order.number += number
    else:
        order = Order(user=User.objects.get(pk=user_id), price=Price.objects.get(pk=price_ud), number=number)
    order.save()
    return HttpResponseRedirect(reverse('food:cart'))


def cart(request):
    orders = Order.objects.filter(has_paid=False).all()
    total = sum([o.number * o.price.value for o in orders])
    user = orders[0].user.name
    context = {'user': user, 'orders': orders, 'total': total}
    return render(request, 'food/cart.html', context)
