# -*- coding: utf-8 -*-
"""
python manage.py makemigrations
python manage.py migrate
"""
from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)
    photo = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Tweet(models.Model):
    author = models.ForeignKey(User)

    type = models.CharField(max_length=200)  # 原创或转发
    publish_date = models.DateTimeField('发布时间')
    title = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    content = models.TextField()
    vote = models.IntegerField("赞", default=0)
    # 菜谱专有字段
    visit = models.IntegerField(default=0)
    score = models.FloatField("评分", default=0)
    # 转发专有字段
    original_id = models.BigIntegerField("菜谱ID", default=0)

    def __unicode__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(User)
    tweet = models.ForeignKey(Tweet)

    content = models.TextField()

    def __unicode__(self):
        return self.content


class Ingredient(models.Model):
    tweet = models.ForeignKey(Tweet)

    name = models.CharField(max_length=200)  # 食材名称
    number = models.IntegerField(default=0)  # 数量
    unit = models.CharField(max_length=200)  # 单位

    def __unicode__(self):
        return ' - '.join([self.tweet.title, self.name])


class Procedure(models.Model):
    tweet = models.ForeignKey(Tweet)

    step = models.IntegerField(default=0)
    picture = models.CharField(blank=True, max_length=200)
    content = models.CharField(max_length=500)

    def __unicode__(self):
        return ' - '.join([self.tweet.title, str(self.step)])


class Supplier(models.Model):
    # 和tweet解耦
    tweet = models.ForeignKey(Tweet)

    name = models.CharField(max_length=200)
    link = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name



