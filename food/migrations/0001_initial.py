# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tweet',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('publish_date', models.DateTimeField(verbose_name=b'date published')),
                ('title', models.CharField(max_length=200)),
                ('logo', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=200)),
                ('visit', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
            ],
        ),
        migrations.AddField(
            model_name='tweet',
            name='user',
            field=models.ForeignKey(to='food.User'),
        ),
    ]
