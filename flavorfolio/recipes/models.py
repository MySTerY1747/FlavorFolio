from django.db import models
from django.contrib.auth.models import User

# Create your models here.
#
#

# class Category(models.Model):
# name = models.CharField(max_length=128, unique=True)
# def __str__(self):
# return self.name
# class Page(models.Model):
# category = models.ForeignKey(Category, on_delete=models.CASCADE)
# title = models.CharField(max_length=128)
# url = models.URLField()
# views = models.IntegerField(default=0)
# def __str__(self):
# return self.title


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images", blank=True)
    bio = models.CharField(blank=True)

    def __str__(self):
        return self.user.username


class Recipe(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    ingredients = models.CharField()
    instructions = models.CharField()
    image = models.ImageField(upload_to="recipe_images", blank=True)
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title} Recipe object"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    content = models.CharField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return self.name
