from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload_recipe/", views.upload_recipe, name="upload_recipe"),
    path("register/", views.register, name="register"),
    path("profile/", views.profile, name="profile"),
    path("recipe/<recipe_id>/", views.recipe, name="recipe"),
    path("profile/edit_bio/", views.edit_bio, name="edit_bio"),
    path("profile/upload_new_profile_picture/", views.upload_new_profile_picture, name="upload_new_profile_picture"),
    path("login/", views.user_login, name="login"),
    path("search/", views.search, name="search"),
]
