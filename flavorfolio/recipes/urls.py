from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path("", views.index, name="index"),
    path("upload_recipe/", views.upload_recipe, name="upload_recipe"),
    path("register/", views.register, name="register"),
    path("logout/", views.user_logout, name="logout"),
    path("profile/<int:user_id>/", views.profile, name="profile"),
    path("profile/", views.user_profile, name="user_profile"),
    path("recipe/<recipe_id>/", views.recipe, name="recipe"),
    path("profile/edit_bio/", views.edit_bio, name="edit_bio"),
    path(
        "profile/upload_new_profile_picture/",
        views.upload_new_profile_picture,
        name="upload_new_profile_picture",
    ),
    path("login/", views.user_login, name="login"),
    path("search/", views.search, name="search"),
    path("tags/<tag_name>/", views.tag, name="tag"),
    path("load_recipes/<int:num_loaded>", views.load_recipes, name="load_recipes"),
    path("delete_account/", views.delete_account, name="delete_account"),
    path("delete_recipe/<int:recipe_id>/", views.delete_recipe, name="delete_recipe"),
    path(
        "update_recipe_image/<int:recipe_id>/",
        views.update_recipe_image,
        name="update_recipe_image",
    ),
    path("add_comment/<int:recipe_id>/", views.add_comment, name="add_comment"),
    path("add_tag/", views.add_tag, name="add_tag"),
    path("recipe/<int:recipe_id>/add_tags/", views.add_tags, name="add_tags"),
]
