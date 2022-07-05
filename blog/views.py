from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic.edit import UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from .models import Recipe, Comment
from django.contrib import messages
from .forms import RecipeForm, CommentForm


@login_required
def add_recipe(request):
    """
    View to add recipe.
    """
    print(request.user)
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
    """
    View to edit recipe.
    """
    model = Recipe
    form_class = RecipeForm
    template_name = 'edit_recipe.html'
    success_url = '/'


class DeleteRecipe(DeleteView):
    """
    View for deletion of recipe.
    """
    model = Recipe
    template_name = 'delete_recipe.html'
    success_url = reverse_lazy('home')


class RecipeList(generic.ListView):
    """
    Recipe list view displays recipes on homepage
    """
    model = Recipe
    queryset = Recipe.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class RecipeDetail(View):
    """
    Recipe detail view to display full recipe when clicked on.
    """    
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
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Recipe.objects.filter(status=1)
        recipe = get_object_or_404(queryset, slug=slug)
        comments = recipe.comments.order_by('created_on')
        liked = False
        if recipe.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.recipe = recipe
            comment.name = request.user
            comment.save()
            messages.success(request, 'Thanks for your comment')

        else:
            comment_form = CommentForm()

        return render(
            request, "recipe_detail.html",
            {
                "recipe": recipe,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class RecipeLike(View):
    """
    Recipe like view displays number of likes for recipe.
    """
    def post(self, request, slug):
        recipe = get_object_or_404(Recipe, slug=slug)

        if recipe.likes.filter(id=request.user.id).exists():
            recipe.likes.remove(request.user)
        else:
            recipe.likes.add(request.user)

        return HttpResponseRedirect(reverse('recipe_detail', args=[slug]))


class DeleteComment(DeleteView):
    """
    Delete comment view.
    """
    model = Comment
    template_name = 'delete_comment.html'
    success_url = reverse_lazy('home')

def about(request):
    return render(request, 'about.html')
