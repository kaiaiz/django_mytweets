# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-04 12:43
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_userprofile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='biography',
            field=models.CharField(blank=True, max_length=200),
        ),
    ]