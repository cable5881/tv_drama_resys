# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-06-04 06:20
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20170518_1244'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='followings',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]
