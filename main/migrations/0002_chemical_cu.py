# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2018-04-11 06:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='chemical',
            name='Cu',
            field=models.CharField(default=3.2, max_length=40),
        ),
    ]
