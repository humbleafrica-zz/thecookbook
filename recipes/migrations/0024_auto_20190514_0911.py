# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-14 09:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0023_auto_20190512_2037'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='update',
            new_name='updated',
        ),
    ]
