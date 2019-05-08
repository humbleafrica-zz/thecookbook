from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
     class Meta:
      model = Recipe
      fields ='__all__'
      
class RawRecipeForm(forms.Form):
    class Meta:
      model = Recipe
      fields ='__all__'