# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-01-31 19:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('markador', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmark',
            name='is_public',
            field=models.BooleanField(default=True, verbose_name='public'),
        ),
    ]