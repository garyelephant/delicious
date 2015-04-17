# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20150417_1129'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('content', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('number', models.IntegerField(default=0)),
                ('unit', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Procedure',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('step', models.IntegerField(default=0)),
                ('photo', models.IntegerField(default=0)),
                ('content', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=200)),
                ('link', models.CharField(max_length=200)),
            ],
        ),
        migrations.RenameField(
            model_name='tweet',
            old_name='user',
            new_name='author',
        ),
        migrations.AddField(
            model_name='tweet',
            name='original_id',
            field=models.BigIntegerField(default=0, verbose_name=b'\xe8\x8f\x9c\xe8\xb0\xb1ID'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='score',
            field=models.FloatField(default=0, verbose_name=b'\xe8\xaf\x84\xe5\x88\x86'),
        ),
        migrations.AddField(
            model_name='tweet',
            name='vote',
            field=models.IntegerField(default=0, verbose_name=b'\xe8\xb5\x9e'),
        ),
        migrations.AddField(
            model_name='user',
            name='photo',
            field=models.CharField(default='a.jpg', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='tweet',
            name='content',
            field=models.TextField(),
        ),
        migrations.AddField(
            model_name='supplier',
            name='tweet',
            field=models.ForeignKey(to='food.Tweet'),
        ),
        migrations.AddField(
            model_name='procedure',
            name='tweet',
            field=models.ForeignKey(to='food.Tweet'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='tweet',
            field=models.ForeignKey(to='food.Tweet'),
        ),
        migrations.AddField(
            model_name='comment',
            name='author',
            field=models.ForeignKey(to='food.User'),
        ),
        migrations.AddField(
            model_name='comment',
            name='tweet',
            field=models.ForeignKey(to='food.Tweet'),
        ),
    ]
