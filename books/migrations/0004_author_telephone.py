# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-01-18 14:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_auto_20170118_1004'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='telephone',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
