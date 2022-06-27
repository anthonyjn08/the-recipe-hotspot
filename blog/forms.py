from .models import Recipe
from django import forms


class AddRecipe(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'featured_image',
            'excerpt',
            'ingredients',
            'instructions',
            'cooking_time',
            'meal_type',
            'meal_tags',
        ]