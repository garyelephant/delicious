from django.db import models


class User(models.Model):
    name = models.CharField(max_length=200)

    def __unicode__(self):
        return self.name


class Tweet(models.Model):
    user = models.ForeignKey(User)
    publish_date = models.DateTimeField('date published')
    title = models.CharField(max_length=200)
    logo = models.CharField(max_length=200)
    content = models.CharField(max_length=200)
    visit = models.IntegerField(default=0)

    def __unicode__(self):
        return self.title