# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-29 15:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cuisineType', models.CharField(choices=[('African', 'African'), ('American', 'American'), ('Australian', 'Australian'), ('British', 'British'), ('Caribbean', 'Caribbean'), ('Chinese', 'Chinese'), ('French', 'French'), ('Greek', 'Greek'), ('Indian', 'Indian'), ('Italian', 'Italian'), ('Japanese', 'Japanese'), ('Mediterranean', 'Mediterranean'), ('Moroccan', 'Moroccan'), ('Spanish', 'Spanish'), ('Thai', 'Thai'), ('Turkish', 'Turkish'), ('Vietnamese', 'Vietnamese'), ('Unknown', 'Unknown')], default='None', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mealType', models.CharField(choices=[('Breakfast', 'Breakfast'), ('Lunch', 'Lunch'), ('Dinner', 'Dinner'), ('Starter', 'Starter'), ('Dessert', 'Dessert')], default='None', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=4000)),
                ('serves', models.IntegerField()),
                ('prep_time', models.DurationField(blank=True, verbose_name='Preparation Time')),
                ('cook_time', models.DurationField(blank=True, verbose_name='Cooking Time')),
                ('ingredients', models.TextField(max_length=1500)),
                ('instructions', models.TextField(max_length=15000)),
                ('suits', models.CharField(max_length=1500)),
                ('calories', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('fat', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('saturates', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('carbs', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('sugars', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('fibre', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('protein', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('salt', models.DecimalField(blank=True, decimal_places=2, default='', max_digits=5)),
                ('created_date', models.DateField(blank=True, verbose_name='Date Created')),
                ('published_date', models.DateField(blank=True, verbose_name='Date Published')),
                ('uploaded_date', models.DateField(blank=True, verbose_name='Date Uploaded')),
                ('cuisineType', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Cuisine')),
                ('mealType', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Meal')),
            ],
        ),
        migrations.CreateModel(
            name='Source',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(blank=True, max_length=25)),
                ('lname', models.CharField(blank=True, max_length=50)),
                ('sourceName', models.CharField(blank=True, max_length=200)),
                ('profession', models.CharField(blank=True, max_length=25)),
                ('sourceCuisine', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Cuisine')),
            ],
        ),
        migrations.CreateModel(
            name='Utensil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('recipeType', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='source',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='recipes.Source'),
        ),
    ]