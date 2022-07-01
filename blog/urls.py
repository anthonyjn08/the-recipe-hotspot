from . import views
from django.urls import path


urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<slug:slug>', views.EditRecipe.as_view(),
                    name='edit_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
]