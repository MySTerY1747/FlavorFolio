from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from recipes.forms import *
from django.shortcuts import get_object_or_404


def index(request):
    context_dict = {"body_block": "This is the index page.", "title_block": "Index"}

    list_of_recipes = sorted(
        Recipe.objects.all(), key=lambda x: x.upload_date, reverse=True
    )
    print(list_of_recipes)

    context_dict["recipes"] = list_of_recipes
    response = render(request, "recipes/index.html", context=context_dict)
    return response


def register(request):
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect("/recipes/profile/")
        else:
            form = RegistrationForm()
    return render(request, "recipes/register.html", {'form': form})


def recipe(request, recipe_id):
    try:
        print(recipe_id)
        current_recipe = Recipe.objects.get(id=recipe_id)
        print(current_recipe)
        return render(
            request, "recipes/recipe.html", context={"recipe": current_recipe}
        )
    except Exception as e:
        return HttpResponse("404. Recipe not found.")


def profile(request,user_id):
    user_profile=UserProfile.objects.get(user_id=user_id)
    print(user_profile.user_id)
    recipes=Recipe.objects.filter(user=user_profile.user)
    context_dict={"user_profile":user_profile,"recipes":recipes}

    return render(request, "recipes/profile.html", context=context_dict)


def upload_recipe(request):
    form = RecipeForm()
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            return redirect("/recipes/<recipe_id>")
        else:
            print(form.errors)
    responce = render(request, "recipes/upload_recipe.html", {'form': form})
    return responce

def edit_bio(request):
    responce = render(request, "recipes/edit_bio.html", context={})

def upload_new_profile_picture(request):
    responce = render(request, "recipes/upload_new_profile_picture.html", context={})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect("/recipes/index/")
            else:
                return HttpResponse("Account is disabled.")
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, 'recipes/login.html')
    
def search(request):
    search_query = request.GET.get('search_query', '')
    if search_query:
        results = Recipe.objects.filter(title=search_query)
    else:
        results = None
    return render(request, 'recipes/search.html', {'results': results, 'search_quesry': search_query})