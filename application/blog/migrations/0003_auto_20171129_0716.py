# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-11-28 23:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_article_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='author',
            field=models.CharField(choices=[(b'linux', b'linux')], default='', max_length=30),
        ),
    ]