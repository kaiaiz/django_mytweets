# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-03 06:39
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20171203_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='slug',
            field=models.SlugField(default=datetime.datetime.now, max_length=250),
        ),
    ]
