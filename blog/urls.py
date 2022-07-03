from . import views
from django.urls import path
from .views import EditRecipe, DeleteRecipe

urlpatterns = [
    path('', views.RecipeList.as_view(), name='home'),
    path('add_recipe/', views.add_recipe, name='add_recipe'),
    path('edit_recipe/<slug:slug>', views.EditRecipe.as_view(),
                    name='edit_recipe'),
    path('delete_recipe/<slug:slug>', views.DeleteRecipe.as_view(),
                    name='delete_recipe'),
    path('<slug:slug>/', views.RecipeDetail.as_view(), name='recipe_detail'),
    path('like/<slug:slug>', views.RecipeLike.as_view(), name='recipe_like'),
    path('delete_comment/<int:pk>', views.DeleteComment.as_view(),
        name='delete_comment'),
]