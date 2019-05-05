from django.conf.urls import url, include
from . import views
from recipes.views import recipe_detail, recipe_add_view

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^breakfast/$', views.breakfast, name='breakfast'),
    url(r'^lunch/$', views.lunch, name='lunch'),
    url(r'^dinner/$', views.dinner, name='dinner'),
    url(r'^dessert/$', views.dessert, name='dessert'),
    url(r'^(?P<pk>[0-9]+)/recipe_detail/$', views.recipe_detail, name='recipe_detail'),
    url(r'^recipe_add/$', views.recipe_add_view, name='recipe_add'),
    url(r'^(?P<pk>[0-9]+)/recipe_delete/$', views.recipe_delete, name='recipe_delete'),
     url(r'^(?P<pk>[0-9]+)/recipe_update/$', views.recipe_update, name='recipe_update'),
]
