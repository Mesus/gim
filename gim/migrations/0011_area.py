# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 10:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gim', '0010_auto_20161125_1256'),
    ]

    operations = [
        migrations.CreateModel(
            name='area',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, null=True)),
                ('lo', models.FloatField(max_length=150)),
                ('la', models.FloatField(max_length=150)),
            ],
        ),
    ]