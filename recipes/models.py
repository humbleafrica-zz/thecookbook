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
    BREAKFAST ='BRE'
    LUNCH = 'LUN'
    DINNER = 'DIN'
    DESSERT = 'DES'
    STARTER = 'STA'
    BRUNCH = 'BRU'
    SNACK = 'SNA'
    MAIN = 'MAI'
    SIDE = 'SID'
    DRINK = 'DRI'
    COCKTAIL = 'COC'
    CANAPE = 'CAN'
    
    RECIPE_TYPE_CHOICES =(
         (BREAKFAST,'Breakfast'),
         (LUNCH,'Lunch'),
         (DINNER,'Dinner'),
         (STARTER,'Starter'),
         (DESSERT,'Dessert'),
         (STARTER, 'Starter'),
         (BRUNCH, 'Brunch'),
         (SNACK, 'Snack'),
         (MAIN, 'Main Course'),
         (SIDE, 'Side Dish'),
         (DRINK, 'Drink'),
         (COCKTAIL, 'Cocktail'),
         (CANAPE, 'Canapé'),
        )
    
    #difficulty choices
    NOVICE ='EAS'
    ADV_BEGINNER = 'NOR'
    COMPETENT = 'HAR'
    EXPERT ='EXP'
    
    DIFF_TYPE_CHOICES =(
        (NOVICE, 'EASY'),
        (ADV_BEGINNER, 'NORMAL'),
        (COMPETENT, 'HARD'),
        (EXPERT, 'EXPERT'),
        )
    
    #publisher choices
    MAGAZINE = 'MAG'
    WEBSITE = 'WEB'
    BOOK = 'BOO'
    SOCIAL_CLUB = 'SOC'
    PROFESSIONAL = 'PRO'
    
    PUBLISHER_CHOICE =(
        (MAGAZINE, 'Magazine'),
        (WEBSITE, 'Website'),
        (BOOK, 'Book'),
        (SOCIAL_CLUB, 'Social Club'),
        (PROFESSIONAL, 'Professional'),
        )
    
    #allergy warnings
    MILK = 'MIL'
    EGG = 'EGG'
    NUT = 'NUT'
    SOYA = 'SOY'
    WHEAT = 'WHE'
    FISH = 'FIS'
    
    ALERGY_CHOICE =(
        (MILK, 'Milk'),
        (EGG, 'Egg'),
        (NUT, 'Nut'),
        (SOYA, 'Soya'),
        (WHEAT, 'Wheat'),
        (FISH, 'Fish'),
        )
    #cuisine type
    
    AFRICAN = 'AF'
    AMERICAN = 'AM'
    ASIAN ='AS'
    AUSTRALIAN = 'AU'
    EUROPEAN = 'EU'
    CARIBBEAN = 'CA'
    MEDITERRANEAN ='ME'
    
    CUISINE_CHOICE =( 
        ('AFRICAN', 'African'),
        ('AMERICAN', 'American'),
        ('ASIAN', 'Asian'),
        ('AUSTRALIAN', 'Australian'),
        ('CARIBBEAN', 'Caribbean'),
        ('EUROPEAN', 'European'),
        ('MEDITERRANEAN', 'Mediterranean'),
        )
    
     # DATABASE FIELDS
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000)
    serves = models.IntegerField()
    prep_time = models.DurationField(u"Preparation Time")
    cook_time = models.DurationField(u"Cooking Time")
    ingredients = models.TextField(max_length=1500)
    instructions = models.TextField(max_length=15000)
    suits = models.CharField(max_length=1500)
    calories = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    fat = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    saturates = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    carbs = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    sugars = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    fibre = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    protein = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    salt = models.DecimalField(max_digits=5, decimal_places=2, default="", blank=True)
    publisher = models.CharField('type', max_length = 3, choices = PUBLISHER_CHOICE)
    allergy = models.CharField('type', max_length = 3, choices = ALERGY_CHOICE)
    difficulty = models.CharField('type', max_length = 3, choices = DIFF_TYPE_CHOICES)
    recipe_type = models.CharField('type', max_length = 3, choices = RECIPE_TYPE_CHOICES)
    cuisine = models.CharField('type', max_length = 3, choices = CUISINE_CHOICE)
    published_date  = models.DateField((u"Date Published"), blank=True)
    uploaded_date = models.DateField((u"Date Uploaded"), blank=True)
    update = models.DateField((u"Last Updated"), blank=True)
    
    # meta class
    class Meta:
        verbose_name = 'recipe'
        verbose_name_plural = 'recipes'
    
    # to string method
    def __str__(self):
         return self.name
         
    #published
    def publish(self):
        self.published_date = timezone.now()
    
    #uploaded
    def uploaded(self):
        self.uploaded_date = timezone.now()
         
    # save method
    def save(self, *args, **kwargs):
      """ add()
        delete()
        update()
        super().save(*args, **kwargs)  # Call the "real" save() method."""
    
    # absolute url method
    def get_absolute_url(self):
        return reverse('company_details', kwargs={'pk': self.id})
