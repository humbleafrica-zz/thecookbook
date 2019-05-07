from django.conf.urls import url, include
from . import views
from recipes.views import recipe_detail

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^breakfast/$', views.breakfast, name='breakfast'),
    url(r'^lunch/$', views.lunch, name='lunch'),
    url(r'^dinner/$', views.dinner, name='dinner'),
    url(r'^dessert/$', views.dessert, name='dessert'),
    url(r'^recipes/recipe/detail/(?P<pk>[0-9]+)/$', views.recipe_detail, name='detail'),
    url(r'^recipes/recipe_add/$', views.recipe_add_view, name='recipe_add'),
    #url(r'^recipe_delete/(?P<pk>[0-9]+)/$', views.recipe_delete, name='recipe_delete'),
]
