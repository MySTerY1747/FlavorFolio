from django.test import TestCase
from django.contrib.auth.models import User
from recipes.models import UserProfile, Recipe
from datetime import datetime

# Create your tests here.
    
def add_recipe(title, ingredients = "", instructions = ""):
    user = User.objects.create_user(username="testuser", password="wz5xe6crtvybu")
    recipe = Recipe.objects.get_or_create(user=user)[0]
    recipe.title = title
    recipe.ingredients = ingredients
    recipe.instructions = instructions
    recipe.save()
    return recipe

class DatabaseRecipeTests(TestCase):

    def test_recipe_upload_date(self):
        test_recipe = add_recipe("Sushi", "this, that", "make it")
        self.assertEqual(datetime.now().strftime("%x"), test_recipe.upload_date.strftime("%x"), "Upload date does not match current date.")