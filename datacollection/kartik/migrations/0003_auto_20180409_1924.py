# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-04-09 19:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kartik', '0002_auto_20180409_1908'),
    ]

    operations = [
        migrations.AlterField(
            model_name='meme',
            name='field_1',
            field=models.FloatField(),
        ),
    ]