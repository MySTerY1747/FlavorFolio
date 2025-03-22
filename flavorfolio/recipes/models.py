from django.db import models
from django.contrib.auth.models import User

#  INFO: For all models, the primary key is automatically created by Django


class UserProfile(models.Model):
    #  username, email, and password are handeld by the Django User model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    picture = models.ImageField(upload_to="profile_images", blank=True)
    bio = models.CharField(max_length=500, blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"


class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    ingredients = models.TextField()
    instructions = models.TextField()
    image = models.ImageField(
        upload_to="recipe_images", blank=True, default="default-recipe.png"
    )
    upload_date = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title}"


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="recipes")
    recipe = models.ForeignKey(
        Recipe, on_delete=models.CASCADE, related_name="comments"
    )
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user.username} on {self.recipe.title}"


class Tag(models.Model):
    name = models.CharField(max_length=128, unique=True)
    recipes = models.ManyToManyField(Recipe)

    def __str__(self):
        return f"{self.name}"

