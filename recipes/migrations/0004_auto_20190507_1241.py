# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-07 12:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20190507_1231'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipe',
            old_name='comments',
            new_name='notes',
        ),
        migrations.AddField(
            model_name='recipe',
            name='author',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]