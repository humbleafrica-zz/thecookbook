from __future__ import unicode_literals
from django.conf import settings
from django.utils import timezone
from django.db import models
from django.conf.urls import include, url
from django.core.urlresolvers import reverse
#from django.urls import reverse

#from django.urls import reverse
# Create your models here.

#recipe model
class Recipe(models.Model):
     #meal choices
    BREAKFAST ='BREAKFAST'
    LUNCH = 'LUNCH'
    DINNER = 'DINNER'
    DESSERT = 'DESSERT'
    STARTER = 'STARTER'
    BRUNCH = 'BRUNCH'
    SNACK = 'SNACK'
    MAIN = 'MAIN'
    SIDE = 'SIDE'
    DRINK = 'DRINK'
    COCKTAIL = 'COCKTAIL'
    CANAPE = 'CANAPE'
    
    RECIPE_TYPE_CHOICES =(
         (BREAKFAST,'BREAKFAST'),
         (LUNCH,'LUNCH'),
         (DINNER,'DINNER'),
         (STARTER,'STARTER'),
         (DESSERT,'DESSERT'),
         (BRUNCH, 'BRUNCH'),
         (SNACK, 'SNACK'),
         (MAIN, 'MAIN COURSE'),
         (SIDE, 'SIDE DISH'),
         (DRINK, 'DRINK'),
         (COCKTAIL, 'COCKTAIL'),
         (CANAPE, 'CANAPE'),
        )
    
    #difficulty choices
    NOVICE ='EASY'
    ADV_BEGINNER = 'NORM'
    COMPETENT = 'HARD'
    EXPERT ='EXPERT'
    
    DIFF_TYPE_CHOICES =(
        (NOVICE, 'EASY'),
        (ADV_BEGINNER, 'NORMAL'),
        (COMPETENT, 'HARD'),
        (EXPERT, 'EXPERT'),
        )
    
    #publisher choices
    MAGAZINE = 'MAGAZINE'
    WEBSITE = 'WEBSITE'
    BOOK = 'BOOK'
    SOCIAL_CLUB = 'SOCIAL CLUB'
    PROFESSIONAL = 'PROFESSIONAL'
    
    PUBLISHER_CHOICE =(
        (MAGAZINE, 'MAGAZINE'),
        (WEBSITE, 'WEBSITE'),
        (BOOK, 'BOOK'),
        (SOCIAL_CLUB, 'SOCIAL CLUB'),
        (PROFESSIONAL, 'PROFESSIONAL'),
        )
    
    #allergy warnings
    MILK = 'MILK'
    EGG = 'EGG'
    NUT = 'NUT'
    SOYA = 'SOYA'
    WHEAT = 'WHEAT'
    FISH = 'FISH'
    PORK = 'PORK'
    ALERGY_CHOICE =(
        (MILK, 'MILK'),
        (EGG, 'EGG'),
        (NUT, 'NUT'),
        (SOYA, 'SOYA'),
        (WHEAT, 'WHEAT'),
        (FISH, 'FISH'),
        (PORK, 'PORK'),
        )
    #cuisine type
    
    AFRICAN = 'AFRICAN'
    AMERICAN = 'AMERICAN'
    ASIAN ='ASIAN'
    AUSTRALIAN = 'AUSTRALIAN'
    EUROPEAN = 'EUROPEAN'
    CARIBBEAN = 'CARIBBEAN'
    MEDITERRANEAN ='MEDITERRANEAN'
    
    CUISINE_CHOICE =( 
        ('AFRICAN', 'AFRICAN'),
        ('AMERICAN', 'AMERICAN'),
        ('ASIAN', 'ASIAN'),
        ('AUSTRALIAN', 'AUSTRALIAN'),
        ('CARIBBEAN', 'CARIBBEAN'),
        ('EUROPEAN', 'EUROPEAN'),
        ('MEDITERRANEAN', 'MEDITERRANEAN'),
        )
    
     # DATABASE FIELDS
    name = models.CharField(max_length=200)
    serves = models.IntegerField()
    prep_time = models.IntegerField(u"Prep Min")
    cook_time = models.IntegerField(u"Cook Min")
    description = models.TextField(max_length=4000)
    ingredients = models.TextField(max_length=1500)
    instructions = models.TextField(max_length=15000)
    suits = models.CharField(max_length=20)
    calories = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    fat = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    saturates = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    carbs = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    sugars = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    fibre = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    protein = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    salt = models.DecimalField(max_digits=4, decimal_places=2, default="", blank=True)
    publisher = models.CharField('publisher', max_length = 20, choices = PUBLISHER_CHOICE)
    allergy = models.CharField('allergy', max_length = 20, choices = ALERGY_CHOICE)
    difficulty = models.CharField('difficulty', max_length = 10, choices = DIFF_TYPE_CHOICES)
    recipe_type = models.CharField('recipe Type', max_length = 20, choices = RECIPE_TYPE_CHOICES)
    cuisine = models.CharField('cuisine', max_length = 20, choices = CUISINE_CHOICE)
    published_date  = models.DateField((u"Date Published"), blank=True)
    uploaded_date = models.DateField((u"Date Uploaded"), blank=True)
    update = models.DateField((u"Last Updated"), blank=True)
    image = models.ImageField(blank=True)
    comments = models.TextField(max_length=1500, blank=True)
    
    # meta class
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'
    
    # to string method
    def __str__(self):
         return self.name
         self.save()
   
    # absolute url method
    def get_absolute_url(self):
        return reverse('recipe_details', kwargs={'pk': self.pk})
  