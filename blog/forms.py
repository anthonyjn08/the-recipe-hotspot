from django_summernote.widgets import SummernoteWidget
from .models import Recipe, Comment
from django import forms


class RecipeForm(forms.ModelForm):
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

        widgets = {
                'ingredients': SummernoteWidget(),
                'instructions': SummernoteWidget(),
            }


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['body']
