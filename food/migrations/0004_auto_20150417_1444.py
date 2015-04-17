# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0003_auto_20150417_1333'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='procedure',
            name='photo',
        ),
        migrations.AddField(
            model_name='procedure',
            name='picture',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
