# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-20 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0010_auto_20171107_0344'),
    ]

    operations = [
        migrations.AddField(
            model_name='photo',
            name='gender',
            field=models.CharField(choices=[('M', 'Male'), ('F', 'Female')], default='M', max_length=1),
            preserve_default=False,
        ),
    ]
