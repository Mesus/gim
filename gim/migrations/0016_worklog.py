# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-08 07:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0015_auto_20161201_1133'),
    ]

    operations = [
        migrations.CreateModel(
            name='worklog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project', models.CharField(max_length=150, null=True)),
                ('people', models.CharField(max_length=150, null=True)),
                ('rq', models.CharField(max_length=150, null=True)),
                ('site', models.CharField(max_length=150, null=True)),
            ],
        ),
    ]
