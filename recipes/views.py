from django.shortcuts import render
from django.utils import timezone #importing the timezone model
from .models import Recipe #importing the recipe model

def index(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/index.html', {'recipes':recipes})