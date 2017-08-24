# -*- coding: utf-8 -*-
# Generated by Django 1.10.7 on 2017-05-08 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meiju', '0009_auto_20170508_1915'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drama',
            name='num_comments',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='num_raters',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='num_star_five',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='num_star_four',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='num_star_one',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='num_star_three',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='num_star_two',
        ),
        migrations.RemoveField(
            model_name='drama',
            name='tv',
        ),
        migrations.AlterField(
            model_name='drama',
            name='current_season',
            field=models.PositiveSmallIntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='drama',
            name='seasons_count',
            field=models.PositiveSmallIntegerField(default=1),
        ),
    ]
