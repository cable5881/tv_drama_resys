# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-27 05:44
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0014_auto_20170527_0846'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewlikes',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='review_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
