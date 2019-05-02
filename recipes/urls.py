from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^breakfast/$', views.breakfast, name='breakfast'),
    url(r'^lunch/$', views.lunch, name='lunch'),
    url(r'^dinner/$', views.dinner, name='dinner'),
    url(r'^dessert/$', views.dessert, name='dessert'),
    url(r'^recipe/$', views.recipe_detail, name='recipe_detail'),
]