from django.shortcuts import render,  get_object_or_404
from django.utils import timezone #importing the timezone model
from recipes.models import Recipe #importing the recipe model

def index(request):
    return render(request, 'recipes/index.html', {})

def breakfast(request):
    return render(request, 'recipes/breakfast.html', {})
    
def lunch(request):
    return render(request, 'recipes/lunch.html', {})

def dinner(request):
    return render(request, 'recipes/dinner.html', {})

def dessert(request):
    return render(request, 'recipes/dessert.html', {})
    
def recipe_detail(request, pk):
    detail = get_object_or_404(Recipe, pk=pk)
    return render(request, 'recipes/recipe_detail.html', {'detail': detail})