from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from recipes.models import Recipe
from recipes.forms import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponseNotAllowed
from django.db.models import Q
from django.db.models import Count


def index(request):
    context_dict = {"body_block": "This is the index page.", "title_block": "Index"}

    list_of_recipes = sorted(
        Recipe.objects.all(), key=lambda x: x.upload_date, reverse=True
    )[:5]
    five_tags = Tag.objects.all()

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
            login(request, user)
            return redirect(reverse("recipes:profile", args=[user.id]))
    return render(request, "recipes/register.html", {"form": form})


def load_recipes(request, num_loaded):
    """
    Loads the next 5 recipes after the ones already displayed.
    Returns them as HTML that can be injected into the page.
    """
    next_recipes = sorted(
        Recipe.objects.all(), key=lambda x: x.upload_date, reverse=True
    )[num_loaded : num_loaded + 5]

    return render(
        request, "recipes/recipe_list_fragment.html", {"recipes": next_recipes}
    )


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
        return HttpResponseNotFound("Recipe not found.")


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse("recipes:index"))


@login_required
def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    recipes = Recipe.objects.filter(user=user_profile.user)
    context_dict = {"user_profile": user_profile, "recipes": recipes}

    return render(request, "recipes/profile.html", context=context_dict)


def profile(request, user_id):
    if request.user.id == user_id:
        return redirect(reverse("recipes:user_profile"))
    else:
        user_profile = UserProfile.objects.get(user_id=user_id)
        recipes = Recipe.objects.filter(user=user_profile.user)
        context_dict = {"user_profile": user_profile, "recipes": recipes}

        return render(request, "recipes/profile.html", context=context_dict)


@login_required
def upload_recipe(request):
    if request.method == "POST":
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()

            # Add existing tags
            for tag in form.cleaned_data["existing_tags"]:
                tag.recipes.add(recipe)

            # Add new tags
            if form.cleaned_data["new_tags"]:
                for tag_name in [
                    name.strip() for name in form.cleaned_data["new_tags"].split(",")
                ]:
                    tag, created = Tag.objects.get_or_create(name=tag_name.title())
                    tag.recipes.add(recipe)

            return redirect(reverse("recipes:recipe", args=[recipe.id]))
    else:
        form = RecipeForm()
    return render(request, "recipes/upload_recipe.html", {"form": form})


@login_required
def edit_bio(request):
    if request.method == "POST":
        form = EditBioForm(request.POST)
        if form.is_valid():
            bio = form.cleaned_data["bio"]
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.bio = bio
            user_profile.save()
            return redirect(reverse("recipes:user_profile"))
    else:
        return render(request, "recipes/edit_bio.html", {"form": EditBioForm()})


@login_required
def upload_new_profile_picture(request):
    if request.method == "POST":
        form = UploadProfilePictureForm(request.POST, request.FILES)
        if form.is_valid():
            new_image = form.cleaned_data["image"]
            user_profile = UserProfile.objects.get(user=request.user)
            user_profile.picture = new_image
            user_profile.save()
            return redirect(reverse("recipes:user_profile"))
        else:
            return HttpResponse(form.errors.as_text())
    else:
        return render(
            request,
            "recipes/upload_new_profile_picture.html",
            {"form": UploadProfilePictureForm()},
        )


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
    search_query = " ".join(request.GET.get("search_query", "").split())
    selected_tags = [tag.strip().title() for tag in request.GET.getlist("tags")]

    results = Recipe.objects.all().prefetch_related("tag_set")

    # Search query filtering
    if search_query:
        results = results.filter(
            Q(title__icontains=search_query) | Q(tag__name__icontains=search_query)
        ).distinct()

    # Tag filtering - require ALL selected tags
    if selected_tags:
        # Create a Q object for each tag and chain them with AND
        for tag in selected_tags:
            results = results.filter(tag__name=tag)

        # Ensure distinct results after multiple filters
        results = results.distinct()

    # Get popular tags with recipe counts
    popular_tags = Tag.objects.annotate(num_recipes=Count("recipes")).order_by(
        "-num_recipes"
    )

    return render(
        request,
        "recipes/search.html",
        {
            "results": [(r, r.tag_set.all()) for r in results],
            "search_query": search_query,
            "all_tags": popular_tags,
            "selected_tags": selected_tags,
        },
    )


def tag(request, tag_name):
    tag = Tag.objects.get(name=tag_name)
    recipes = tag.recipes.all()
    return render(request, "recipes/tag.html", {"tag": tag, "recipes": recipes})


@login_required
def delete_account(request):
    if request.method == "POST":
        user = request.user
        logout(request)
        user.delete()
        return redirect(reverse("recipes:index"))
    return HttpResponseNotAllowed(["POST"])


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        # Verify user owns the recipe
        if request.user != recipe.user:
            return HttpResponse("Unauthorized", status=401)

        recipe.delete()
        return redirect(reverse("recipes:user_profile"))

    return HttpResponseNotAllowed(["POST"])


@login_required
def delete_recipe(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        # Verify user owns the recipe
        if request.user != recipe.user:
            return HttpResponse("Unauthorized", status=401)

        recipe.delete()
        return redirect(reverse("recipes:user_profile"))

    return HttpResponseNotAllowed(["POST"])


@login_required
def update_recipe_image(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.user != recipe.user:
        return HttpResponse("Unauthorized", status=401)

    if request.method == "POST":
        form = RecipeImageForm(request.POST, request.FILES, instance=recipe)
        if form.is_valid():
            form.save()

    return redirect(reverse("recipes:recipe", args=[recipe_id]))


@login_required
def add_comment(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user
            comment.recipe = recipe
            comment.save()

    return redirect(reverse("recipes:recipe", args=[recipe_id]))


@login_required
def add_tag(request):
    if request.method == "POST":
        form = AddTagForm(request.POST)
        if form.is_valid():
            try:
                tag = form.save(commit=False)
                tag.name = tag.name.title()
                if tag.name in [t.name for t in Tag.objects.all()]:
                    return HttpResponse("This tag already exists")
                tag.save()
                return redirect(reverse("recipes:tag", args=[tag.name]))
            except Exception as e:
                form.add_error("name", "This tag already exists!")
    else:
        form = AddTagForm()
    return render(request, "recipes/add_tag.html", {"form": form})


@login_required
def add_tags(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    if request.method == "POST":
        form = AddTagsForm(request.POST)
        if form.is_valid():
            # Add existing tags
            for tag in form.cleaned_data["existing_tags"]:
                tag.recipes.add(recipe)

            # Add new tags
            if form.cleaned_data["new_tags"]:
                for tag_name in [
                    name.strip() for name in form.cleaned_data["new_tags"].split(",")
                ]:
                    tag, created = Tag.objects.get_or_create(name=tag_name.title())
                    tag.recipes.add(recipe)

            return redirect(reverse("recipes:recipe", args=[recipe_id]))
    else:
        form = AddTagsForm()
    return render(request, "recipes/add_tags.html", {"form": form, "recipe": recipe})
