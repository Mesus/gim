# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-25 04:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0009_auto_20161125_1128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='erp_data',
            name='btfjs',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='erp_data',
            name='dj',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='erp_data',
            name='fjs',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='erp_data',
            name='hsdj',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='erp_data',
            name='jshj',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='erp_data',
            name='sl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='erp_data',
            name='slsl',
            field=models.CharField(max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='erp_data',
            name='tlsl',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
