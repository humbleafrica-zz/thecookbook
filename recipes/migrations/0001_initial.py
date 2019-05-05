# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-05-05 13:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('serves', models.IntegerField()),
                ('prep_time', models.IntegerField(verbose_name='Prep Min')),
                ('cook_time', models.IntegerField(verbose_name='Cook Min')),
                ('description', models.TextField(max_length=4000)),
                ('ingredients', models.TextField(max_length=1500)),
                ('instructions', models.TextField(max_length=15000)),
                ('suits', models.CharField(max_length=20)),
                ('calories', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('fat', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('saturates', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('carbs', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('sugars', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('fibre', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('protein', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('salt', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=4)),
                ('publisher', models.CharField(choices=[('MAGAZINE', 'MAGAZINE'), ('WEBSITE', 'WEBSITE'), ('BOOK', 'BOOK'), ('SOCIAL CLUB', 'SOCIAL CLUB'), ('PROFESSIONAL', 'PROFESSIONAL')], max_length=20, verbose_name='publisher')),
                ('allergy', models.CharField(choices=[('MILK', 'MILK'), ('EGG', 'EGG'), ('NUT', 'NUT'), ('SOYA', 'SOYA'), ('WHEAT', 'WHEAT'), ('FISH', 'FISH'), ('PORK', 'PORK')], max_length=20, verbose_name='allergy')),
                ('difficulty', models.CharField(choices=[('EASY', 'EASY'), ('NORM', 'NORMAL'), ('HARD', 'HARD'), ('EXPERT', 'EXPERT')], max_length=10, verbose_name='difficulty')),
                ('recipe_type', models.CharField(choices=[('BREAKFAST', 'BREAKFAST'), ('LUNCH', 'LUNCH'), ('DINNER', 'DINNER'), ('STARTER', 'STARTER'), ('DESSERT', 'DESSERT'), ('STARTER', 'STARTER'), ('BRUNCH', 'BRUNCH'), ('SNACK', 'SNACK'), ('MAIN', 'MAIN COURSE'), ('SIDE', 'SIDE DISH'), ('DRINK', 'DRINK'), ('COCKTAIL', 'COCKTAIL'), ('CANAPE', 'CANAPE')], max_length=20, verbose_name='recipe Type')),
                ('cuisine', models.CharField(choices=[('AFRICAN', 'AFRICAN'), ('AMERICAN', 'AMERICAN'), ('ASIAN', 'ASIAN'), ('AUSTRALIAN', 'AUSTRALIAN'), ('CARIBBEAN', 'CARIBBEAN'), ('EUROPEAN', 'EUROPEAN'), ('MEDITERRANEAN', 'MEDITERRANEAN')], max_length=20, verbose_name='cuisine')),
                ('published_date', models.DateField(blank=True, verbose_name='Date Published')),
                ('uploaded_date', models.DateField(blank=True, verbose_name='Date Uploaded')),
                ('update', models.DateField(blank=True, verbose_name='Last Updated')),
                ('image', models.ImageField(blank=True, upload_to=b'')),
                ('comments', models.TextField(blank=True, max_length=1500)),
            ],
            options={
                'verbose_name': 'recipe',
                'verbose_name_plural': 'recipes',
            },
        ),
    ]
