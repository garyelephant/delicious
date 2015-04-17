# -*- coding: utf-8 -*-
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Tweet(models.Model):
    user = models.ForeignKey(User)
    type = models.CharField(max_length=200)  # 原创或转发
    publish_date = models.DateTimeField('发布时间')
    title = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    visit = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title