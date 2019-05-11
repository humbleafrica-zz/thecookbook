from django.conf.urls import url, include
from . import views
from recipes.views import(
    index,
    breakfast,
    lunch,
    dinner,
    dessert,
    recipe_add,
    recipe_delete,
    recipe_detail,
    recipes,
    preparation,
    register,
    like_recipe,)

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^breakfast/$', views.breakfast, name='breakfast'),
    url(r'^lunch/$', views.lunch, name='lunch'),
    url(r'^dinner/$', views.dinner, name='dinner'),
    url(r'^dessert/$', views.dessert, name='dessert'),
    url(r'^recipes/recipe/detail/(?P<pk>[0-9]+)/$', views.recipe_detail, name='detail'),
    url(r'^recipes/recipe_add/$', views.recipe_add, name='recipe_add'),
    url(r'^recipes/recipe/allrecipes/$', views.recipes, name='allrecipes'), 
    url(r'^recipes/recipe/preparation/(?P<pk>[0-9]+)/$', views.preparation, name='preparation'),
    url(r'^recipes/recipe/recipe_update/(?P<pk>[0-9]+)/$', views.recipe_update, name='recipe_update'),
    url(r'^recipes/recipe_delete/(?P<pk>[0-9]+)/$', views.recipe_delete, name='recipe_delete'),
    url(r'^register/$', views.register, name='register'),
    url(r'^like/$', views.like_recipe, name='like_recipe'),
]

