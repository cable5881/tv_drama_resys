# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 12:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meiju', '0010_auto_20170508_2008'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drama',
            name='pubdate',
        ),
    ]
