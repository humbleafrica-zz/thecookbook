# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-07 12:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0005_auto_20190507_1242'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='scalable',
            field=models.BooleanField(default=True),
        ),
    ]
