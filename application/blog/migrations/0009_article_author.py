# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-12-04 12:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_remove_article_author'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='author',
            field=models.CharField(choices=[(b'linux', b'linux')], default='', max_length=30),
        ),
    ]
