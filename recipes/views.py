from django.shortcuts import render, render_to_response,  get_object_or_404
from django.utils import timezone #importing the timezone model
from recipes.models import Recipe #importing the recipe model
from forms import RecipeForm

#add recipe view
def recipe_add_view(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = RecipeForm()
        
    context ={
        'form': form,
    }
    return render(request, 'recipes/recipe_add.html', context)
       

#index view
def index(request):
    return render(request, 'recipes/index.html', {})

#breakfast view
def breakfast(request, pk):
    brk= get_object_or_404(Recipe, pk=pk)
    context ={
        'breakfast': brk,
    }
    return render(request, 'recipes/breakfast.html', context)

#lunch view
def lunch(request):
    return render(request, 'recipes/lunch.html', {})

#dinner view
def dinner(request):
    return render(request, 'recipes/dinner.html', {})

#dessert view
def dessert(request):
    return render(request, 'recipes/dessert.html', {})

#recipe_detail view
def recipe_detail(request, pk):
    obj= get_object_or_404(Recipe, pk=pk)
    context ={
        'recipe': obj,
    }
    return render(request, 'recipes/recipe/recipe_detail.html', context)
    