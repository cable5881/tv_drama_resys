# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-09 11:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meiju', '0015_auto_20170509_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drama',
            name='types',
            field=models.ManyToManyField(related_name='types', to='meiju.DramaType'),
        ),
    ]
