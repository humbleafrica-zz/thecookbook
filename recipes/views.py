from django.shortcuts import render, render_to_response,  get_object_or_404, redirect
from django.utils import timezone #importing the timezone model
from recipes.models import Recipe #importing the recipe model
from forms import RecipeForm


#index view###################################################
def index(request):
    return render(request, 'recipes/index.html', {})

#breakfast view###################################################
def breakfast(request):
    queryset = Recipe.objects.filter(recipe_type='BREAKFAST')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/breakfast.html', context)

#lunch view###################################################
def lunch(request):
    queryset = Recipe.objects.filter(recipe_type='LUNCH')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/lunch.html', context)

#dinner view###################################################
def dinner(request):
    queryset = Recipe.objects.filter(recipe_type='DINNER')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/dinner.html', context)

#dessert view###################################################
def dessert(request):
    queryset = Recipe.objects.filter(recipe_type='DESSERT')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/dessert.html', context)

#starter view###################################################
def starter(request):
    queryset = Recipe.objects.filter(recipe_type='STARTER')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/starter.html', context)

#starter view###################################################
def brunch(request):
    queryset = Recipe.objects.filter(recipe_type='BRUNCH')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/brunch.html', context)
    
#snack view###################################################
def snack(request):
    queryset = Recipe.objects.filter(recipe_type='SNACK')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/snack.html', context)
    
#main view###################################################
def main(request):
    queryset = Recipe.objects.filter(recipe_type='MAIN')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/main.html', context)
    
#side view###################################################
def side(request):
    queryset = Recipe.objects.filter(recipe_type='SIDE')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/side.html', context)
    
#drink view###################################################
def drink(request):
    queryset = Recipe.objects.filter(recipe_type='DRINK')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/drink.html', context)

#cocktail view###################################################
def cocktail(request):
    queryset = Recipe.objects.filter(recipe_type='COCKTAIL')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/cocktail.html', context)

#canape view###################################################
def canape(request):
    queryset = Recipe.objects.filter(recipe_type='CANAPE')
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/canape.html', context)

#recipe_detail view###################################################
def recipe_detail(request, pk):
    obj= get_object_or_404(Recipe, pk=pk)
    context ={
        'recipe': obj,
    }
    return render(request, 'recipes/recipe/recipe_detail.html', context)
    
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

#update recipe view
def recipe_update(request, pk):
    queryset = Recipe.objects.filter(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, initial=queryset)
    if request.method == 'POST':
        form.save()
        alert('Recipe Saved')
        #form = RecipeForm()
    context ={
        'form': form,
    }
    
    return render(request, 'recipes/recipe_update.html', context)
     
#recipe_delete view###################################################
def recipe_delete(request, pk):
    obj= get_object_or_404(Recipe, pk=pk)
    form = RecipeForm(request.POST or None, initial=obj)
    #confirming delte
    if request.method == 'POST':
        obj.delete()
        return redirect('../../')
    context ={
        'form': form,
    }
    return render(request, 'recipes/recipe/recipe_delete.html', context)
    