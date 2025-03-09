from django.urls import path
from recipes import views

app_name = "recipes"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("upload_recipe", views.upload_recipe, name="upload_recipe"),
    path("register/", views.register, name="register"),
]
