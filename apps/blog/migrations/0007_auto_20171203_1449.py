# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-03 06:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20171203_1447'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='created_time',
            field=models.DateField(auto_now_add=True),
        ),
    ]
