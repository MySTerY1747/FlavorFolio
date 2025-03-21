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
    five_tags = Tag.objects.all()[:5]

    context_dict["recipes"] = list_of_recipes
    context_dict["tags"] = five_tags
    response = render(request, "recipes/index.html", context=context_dict)
    return response


def register(request):
    form = RegistrationForm()
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.set_password(user.password)
            user.save()
            UserProfile.objects.create(user=user)
            return redirect(reverse("recipes:profile", args=[user.id]))
        else:
            print(form.errors)
            form = RegistrationForm()
    return render(request, "recipes/register.html", {"form": form})


def recipe(request, recipe_id):
    try:
        recipe_tags = Tag.objects.filter(recipes=recipe_id)
        current_recipe = Recipe.objects.get(id=recipe_id)
        current_recipe_comments = Comment.objects.filter(recipe=current_recipe)
        return render(
            request,
            "recipes/recipe.html",
            context={
                "recipe": current_recipe,
                "comments": current_recipe_comments,
                "tags": recipe_tags,
            },
        )
    except Exception as e:
        return HttpResponse("404. Recipe not found.")


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("recipes:index"))


def profile(request, user_id):
    user_profile = UserProfile.objects.get(user_id=user_id)
    print(user_profile.user_id)
    recipes = Recipe.objects.filter(user=user_profile.user)
    context_dict = {"user_profile": user_profile, "recipes": recipes}

    return render(request, "recipes/profile.html", context=context_dict)


@login_required
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
    responce = render(request, "recipes/upload_recipe.html", {"form": form})
    return responce


@login_required
def edit_bio(request):
    responce = render(request, "recipes/edit_bio.html", context={})


@login_required
def upload_new_profile_picture(request):
    responce = render(request, "recipes/upload_new_profile_picture.html", context={})


def user_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse("recipes:index"))
            else:
                return HttpResponse("Account is disabled.")
        else:
            return HttpResponse("Invalid login details.")
    else:
        return render(request, "recipes/login.html")


def search(request):
    search_query = request.GET.get("search_query", "")
    tag = request.GET.get("tag", "")
    results_set = set()
    if search_query:
        title_matches = Recipe.objects.filter(title__icontains=search_query)
        tag_matches = Tag.objects.filter(name__icontains=search_query)
        tag_recipes = Recipe.objects.filter(
            id__in=tag_matches.values_list("recipes", flat=True)
        )
        results_set.update(title_matches)
        results_set.update(tag_recipes)

    results = (
        [(recipe, Tag.objects.filter(recipes=recipe)) for recipe in results_set]
        if results_set
        else None
    )

    return render(
        request,
        "recipes/search.html",
        {"results": results, "search_query": search_query, "tags": tag},
    )


def tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    recipes = tag.recipes.all()
    return render(request, "recipes/tag.html", {"tag": tag, "recipes": recipes})
