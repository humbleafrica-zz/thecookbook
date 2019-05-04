# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-04 12:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0006_auto_20190504_1221'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='cuisine',
            field=models.CharField(choices=[('AFRICAN', 'AFRICAN'), ('AMERICAN', 'AMERICAN'), ('ASIAN', 'ASIAN'), ('AUSTRALIAN', 'AUSTRALIAN'), ('CARIBBEAN', 'CARIBBEAN'), ('EUROPEAN', 'EUROPEAN'), ('MEDITERRANEAN', 'MEDITERRANEAN')], max_length=20, verbose_name='cuisine'),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='recipe_type',
            field=models.CharField(choices=[('BREAKFAST', 'BREAKFAST'), ('LUNCH', 'LUNCH'), ('DINNER', 'DINNER'), ('STARTER', 'STARTER'), ('DESSERT', 'DESSERT'), ('STARTER', 'STARTER'), ('BRUNCH', 'BRUNCH'), ('SNACK', 'SNACK'), ('MAIN', 'MAIN COURSE'), ('SIDE', 'SIDE DISH'), ('DRINK', 'DRINK'), ('COCKTAIL', 'COCKTAIL'), ('CANAPE', 'CANAPE')], max_length=20, verbose_name='recipe Type'),
        ),
    ]