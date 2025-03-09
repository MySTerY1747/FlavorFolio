from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.forms import RecipeForm


def index(request):
    context_dict = {"body_block": "This is the index page.", "title_block": "Index"}
    response = render(request, "recipes/base.html", context=context_dict)
    return response


def about(request):
    context_dict = {"body_block": "This is the about page.", "title_block": "About"}
    response = render(request, "recipes/base.html", context=context_dict)
    return response

def upload_recipe(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect('/recipes/<recipe_id>')
        else:
            print(form.errors)
    responce = render(request, "recipes/upload_recipe.html", {'form': form})
    return responce