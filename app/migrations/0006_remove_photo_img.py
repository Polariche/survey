# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-10-19 17:55
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20171020_0002'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='photo',
            name='img',
        ),
    ]
