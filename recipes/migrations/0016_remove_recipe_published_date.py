# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-10 11:44
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0015_auto_20190510_1136'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='published_Date',
        ),
    ]
