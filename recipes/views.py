from django.shortcuts import render, render_to_response,  get_object_or_404, redirect
from django.utils import timezone #importing the timezone model
from datetime import datetime, timedelta # import to filter new recipes
from .models import Recipe #importing the recipe model
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.core.urlresolvers import reverse_lazy
from forms import RecipeForm #RawRecipeForm
from django.contrib.auth.forms import UserCreationForm #import to use the builtin user creation form



#index view###################################################
def index(request):
    queryset = Recipe.objects.all()
    context={
        "object_list": queryset,
        'index': 'active'
    }
    return render(request, 'recipes/index.html', context)

###recipe data for chart####
def get_recipe_data(request):
    recipes = Recipe.objects.all().count()
    b = Recipe.objects.filter(recipe_type='BREAKFAST').count()
    l = Recipe.objects.filter(recipe_type='LUNCH').count()
    d = Recipe.objects.filter(recipe_type='DINNER').count()
    
    labels=['BRK','LUN', 'DIN']
    default_items =[b, l, d]
    
    recipe_data = {
       'labels': labels,
       'default' : default_items,
    }
    return JsonResponse(recipe_data)
    
######cuidine dat for charts##### 
def get_cuisine_data(request):
    
    af = Recipe.objects.filter(cuisine='AFRICAN').count()
    am = Recipe.objects.filter(cuisine='AMERICAN').count()
    at = Recipe.objects.filter(cuisine='ASIAN').count()
    au = Recipe.objects.filter(cuisine='AUSTRALIAN').count()
    ca = Recipe.objects.filter(cuisine='CARIBBEAN').count()
    eu = Recipe.objects.filter(cuisine='EUROPEAN').count()
    me = Recipe.objects.filter(cuisine='MEDITERRANEAN').count()
    
    labels=['AFR','AMR','ASI', 'AUS','CAR','EUR', 'MED']
    default_items =[af, am, at, au, ca, eu, me]

    cuisine_data = {
        'labels': labels,
        'default' : default_items,
    }
    return JsonResponse(cuisine_data)

#######allergy filter ##########
def get_allergy_data(request):
    mk = Recipe.objects.filter(allergy='MILK').count()
    eg = Recipe.objects.filter(allergy='EGG').count()
    nu = Recipe.objects.filter(allergy='NUT').count()
    so = Recipe.objects.filter(allergy='SOYA').count()
    wh = Recipe.objects.filter(allergy='WHEAT').count()
    fi = Recipe.objects.filter(allergy='FISH').count()
    po = Recipe.objects.filter(allergy='PORK').count()
    
    labels=['Milk','Egg','Nut', 'Soya','Wheat','Fish', 'Pork']
    default_items =[mk, eg, nu, so, wh, fi, po]
    
    allergy_data = {
        'labels': labels,
        'default' : default_items,
    }
    return JsonResponse(allergy_data)
    
#breakfast view###################################################
def breakfast(request):
    queryset = Recipe.objects.filter(recipe_type='BREAKFAST')
    context={
        "object_list": queryset,
        'breakfast': 'active'
    }
    return render(request, 'recipes/breakfast.html', context)

#lunch view###################################################
def lunch(request):
    queryset = Recipe.objects.filter(recipe_type='LUNCH')
    context={
        "object_list": queryset,
        'lunch': 'active'
    }
    return render(request, 'recipes/lunch.html', context)

#dinner view###################################################
def dinner(request):
    queryset = Recipe.objects.filter(recipe_type='DINNER')
    context={
        "object_list": queryset,
        'dinner': 'active'
    }
    return render(request, 'recipes/dinner.html', context)

#dessert view###################################################
def dessert(request):
    queryset = Recipe.objects.filter(recipe_type='DESSERT')
    context={
        "object_list": queryset,
        'dessert': 'active'
    }
    return render(request, 'recipes/dessert.html', context)

#starter view###################################################
def starter(request):
    queryset = Recipe.objects.filter(recipe_type='STARTER')
    context={
        "object_list": queryset,
        'starter': 'active'
    }
    return render(request, 'recipes/starter.html', context)

#starter view###################################################
def brunch(request):
    queryset = Recipe.objects.filter(recipe_type='BRUNCH')
    context={
        "object_list": queryset,
        'brunch': 'active'
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
def recipe_detail(request,pk):
    queryset = Recipe.objects.filter(pk=pk)
    recipe = get_object_or_404(Recipe, pk=pk)
    is_liked = False
    if recipe.likes.filter(id=request.user.id).exists():
        is_liked = True
    context={
        "object_list": queryset,
        'is_liked' : is_liked,
        'total_likes': recipe.total_likes(),
        'recipe':recipe,
    }
    return render(request, 'recipes/detail.html', context)
    
#recipe_like view###################################################
def like_recipe(request):
    name = get_object_or_404(Recipe, id=request.POST.get('recipe_id'))
    is_liked = False
    if name.likes.filter(id=request.user.id).exists():
        name.likes.remove(request.user)
        is_liked = False
    else:
        name.likes.add(request.user)
        is_liked = True
    return HttpResponseRedirect(name.get_absolute_url())

#recipe_preparationview###################################################
def preparation(request,pk):
    queryset = Recipe.objects.filter(pk=pk)
    context={
        "object_list": queryset
    }
    return render(request, 'recipes/preparation.html', context)
    
#add recipe view
def recipe_add(request):
    form = RecipeForm(request.POST or None)
    if form.is_valid():
        pic = form.cleaned_data['image']
        user= request.user
        form.save()
        form = RecipeForm()
    context ={
        'form': form,
    }
    return render(request, 'recipes/recipe_add.html', context)
   
#return all recipes
def recipes(request):
    queryset = Recipe.objects.all()
    query =request.GET.get('q')
    if query:
        recipe = Recipe.objects.filter(
            Q(name__contains=query)|
            Q(author__contains=query)|
            Q(country__contains=query)
            )
    context={
        "object_list": queryset,
        'search_list': query
    }
    return render(request, 'recipes/all.html', context)
    
#update recipe view
def recipe_update(request, pk):
    #retrieve RecipeForm() data
    obj = Recipe.objects.get(pk=pk)
    form = RecipeForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    context ={
        'form': form,
    }
    return render(request, 'recipes/recipe/update.html', context) 
     
#recipe_delete view###################################################
def recipe_delete(request, pk):
    obj= get_object_or_404(Recipe, pk=pk)
    #form = RecipeForm(request.POST or None, initial=obj)
    #confirming delte
    if request.method == 'POST':
        obj.delete()
        return redirect('/')
    context ={
        'object': obj,
    }
    return render(request, 'recipes/recipe_delete.html', context)
    
def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    else:
        form = UserCreationForm()
    
    context ={
        'form': form,
        'signup': 'signup',
    }
    
    return render(request, 'registration/reg_form.html', context)