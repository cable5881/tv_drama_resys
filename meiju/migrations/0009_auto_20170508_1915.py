# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meiju', '0008_auto_20170508_0933'),
    ]

    operations = [
        migrations.AddField(
            model_name='drama',
            name='alternate_name',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='drama',
            name='current_season',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='drama',
            name='douban_url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='drama',
            name='seasons_count',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
