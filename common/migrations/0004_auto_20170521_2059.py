# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-21 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0003_auto_20170521_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dish',
            name='weight',
            field=models.CharField(default='', max_length=100),
        ),
    ]
