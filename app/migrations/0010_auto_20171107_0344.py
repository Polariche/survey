# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-06 18:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20171107_0320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='score',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)], default=0),
        ),
    ]
