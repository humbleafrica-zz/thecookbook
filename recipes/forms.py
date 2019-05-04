from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
     #name = forms.CharField(required=True),
     #description = forms.CharField(
      #   required=True, 
       #  widget=forms.TextInput(
        #     attrs={
         #        "placeholder": "description",
          #       "class":"",
           #      "id":"",
                 
            # })
             #   ),
             class Meta:
                 model = Recipe
                 fields =[
                'name',
                'description',
                'serves',
                'prep_time',
                'cook_time',
                'ingredients',
                'instructions',
                'suits',
                'calories',
                'fat',
                'saturates',
                'carbs',
                'sugars',
                'fibre',
                'protein',
                'salt',
                'publisher',
                'allergy',
                'difficulty',
                'recipe_type',
                'cuisine',
                'published_date',
                'uploaded_date',
                'update',
                'image',
                ]
        
           