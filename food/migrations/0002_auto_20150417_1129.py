# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='type',
            field=models.CharField(default='cookbook', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='publish_date',
            field=models.DateTimeField(verbose_name=b'\xe5\x8f\x91\xe5\xb8\x83\xe6\x97\xb6\xe9\x97\xb4'),
        ),
    ]
