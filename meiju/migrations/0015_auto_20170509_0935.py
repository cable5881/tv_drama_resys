# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-09 01:35
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('meiju', '0014_remove_drama_website'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='writer',
            name='drama',
        ),
        migrations.DeleteModel(
            name='Writer',
        ),
    ]