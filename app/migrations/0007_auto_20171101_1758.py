# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-11-01 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_remove_photo_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vote',
            name='photo',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='vote',
            name='voter',
            field=models.IntegerField(),
        ),
    ]