# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 12:19
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meiju', '0011_remove_drama_pubdate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drama',
            name='country',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='language',
        ),
    ]
