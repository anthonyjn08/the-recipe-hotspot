from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Recipe
from .forms import RecipeForm


def add_recipe(request):
    recipe_form = RecipeForm(request.POST, request.FILES)

    if request.method == 'POST':
        if recipe_form.is_valid():
            recipe_form = recipe_form.save(commit=False)
            recipe_form.title = recipe_form.title
            recipe_form.author = request.user
            recipe_form.status = 1
            recipe_form.save()
            return redirect(reverse('home'))

    context = {
        'recipe_form': recipe_form
    }

    return render(request, 'add_recipe.html', context)
    

class EditRecipe(UpdateView):
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'
    success_url = '/'


class DeleteRecipe(DeleteView):
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')


class RecipeList(generic.ListView):
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    
    def get(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('-created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True
        
        return render(
            request,
            "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked
            }
        )
