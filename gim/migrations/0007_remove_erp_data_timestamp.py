# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 03:10
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0006_auto_20161125_1109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='erp_data',
            name='timestamp',
        ),
    ]
