# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-10 11:34
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0012_auto_20190510_1133'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='published_Date',
            new_name='published_date',
        ),
    ]
