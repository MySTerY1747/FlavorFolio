import os
import django
from django.core.files import File

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "flavorfolio.settings")
django.setup()

from recipes.models import UserProfile, Tag, Recipe, Comment, User

users = [
    {
        "username": "Rob the chef",
        "email": "chefrob@email.com",
        "bio": "I am another chef",
    },
    {
        "username": "Bob the chef",
        "email": "chefbob@email.com",
        "bio": "I am yet another chef",
    },
    {
        "username": "Marina the home cook",
        "email": "marina@someemail.com",
        "bio": "I am a home cook",
        "image_path":"population_script_images/marina.jpg"
    },
]

recipes = [
    #  INFO: These are genuinely my own recipes
    {
        "user_index": 0,
        "title": "Fasolada (Traditional Greek Bean Soup)",
        "ingredients": "- 1 onion\n - 1 clove garlic\n - 1 carrot\n - Tomato purée\n - White beans\n - Olive oil\n - Salt\n - Pepper\n - Bay leaf\n - Rosemary\n - 1 vegetable stock cube\n - 1 apple\n - Water\n - Vinegar",
        "instructions": "- Finely chop the onion, garlic, and carrot.\n - Add them to a pot with olive oil and sauté.\n - Stir in tomato purée, salt, pepper, bay leaf, and rosemary.\n - Add a vegetable stock cube and a whole apple.\n - Fill the pot with water until ingredients are covered.\n - Simmer on low heat for 1.5 hours.\n - Adjust seasoning with more salt, pepper, olive oil, and a splash of vinegar before serving.",
        "image_path": "population_script_images/fasolada.jpg",
    },
    {
        "user_index": 1,
        "title": "Greek Salad",
        "ingredients": "- 3 tomatoes\n - 1 cucumber\n - half an onion\n - Feta\n - Olive oil\n - Honey\n - Vinegar\n - Olives\n - Green pepper ",
        "instructions": " - Cut the tomatoes into nice pieces, removing the stem\n - Add salt and mix\n - In a bowl, add some honey and vinegar to make a sweet and sour sauce\n - Cut the cucumber into strips, checking first whether or not to remove the peel\n - Cut the side of a pepper into strips\n - Cut half an onion into thin slices, and dip them in the bowl, with the sauce\n - Add a few olives\n - Put a nice piece of feta cheese on top\n - Add pepper, oregano\n - Finally, pour olive oil EVERYWHERE. ",
        "image_path": "population_script_images/xoriatiki-salata.jpg",
    },
    {
        "user_index": 2,
        "title": "Kokkinisti Tigania Manitarion (Greek Mushroom Sauté in Tomato Sauce)",
        "ingredients": "- Olive oil\n - 1 onion\n - 1 red pepper\n - 1 green pepper\n - 1 clove garlic\n - Salt\n - Pepper\n - 500g mushrooms\n - Tomato purée\n - Red wine\n - Oregano\n - Thyme\n - Sugar",
        "instructions": "- Chop the onion and add it to a pan with olive oil.\n - Slice the red and green peppers and add them to the pan.\n - Add a clove of garlic and stir.\n - Add thyme and mix well.\n - While sautéing, chop the mushrooms.\n - Remove everything from the pan and set aside.\n - Add more olive oil and cook the mushrooms until they develop a nice color.\n - Return the sautéed vegetables to the pan.\n - Season with salt, pepper, and other spices.\n - Add tomato purée, red wine, oregano, and a little sugar.\n - Let it simmer briefly, then serve.",
        "image_path": "population_script_images/tigania-manitarion-kokkinisti.jpg",
    },
]

tags = [
    {
        "name": "Greek",
        "recipe_indices": [0, 1, 2],
    },
    {
        "name": "Vegetarian",
        "recipe_indices": [0, 1, 2],
    },
    {
        "name": "Vegan",
        "recipe_indices": [0, 2],
    },
]

comments = [
    {
        "content": "Whoa! That looks amazing! I'll have to try it out soon.",
        "user_index": 1,
        "recipe_index": 0,
    },
    {
        "content": "Are you sure you really need THAT much olive oil haha?",
        "user_index": 2,
        "recipe_index": 1,
    },
    {
        "content": "I didn't know you could use an apple in a bean soup! Does it impact the flavor at all?",
        "user_index": 2,
        "recipe_index": 0,
    },
]


def add_user(user_dict):

    user_model = User.objects.get_or_create(
        username=user_dict["username"], email=user_dict["email"]
    )[0]
    
    try:
        user = UserProfile.objects.get_or_create(user=user_model, bio=user_dict["bio"],picture=user_dict["image_path"])[0]
    except:
        user = UserProfile.objects.get_or_create(user=user_model, bio=user_dict["bio"])[0]

    user.save()
    return user


def add_recipe(recipe_dict):
    with open(recipe_dict["image_path"], "rb") as f:
        recipe = Recipe.objects.get_or_create(
            user=User.objects.all()[recipe_dict["user_index"]],
            title=recipe_dict["title"],
            ingredients=recipe_dict["ingredients"],
            instructions=recipe_dict["instructions"],
            image=File(f, name=os.path.basename(recipe_dict["image_path"])),
        )[0]
        recipe.save()
    return recipe


def add_comment(comment_dict):
    comment = Comment.objects.get_or_create(
        user=User.objects.all()[comment_dict["user_index"]],
        recipe=Recipe.objects.all()[comment_dict["recipe_index"]],
        content=comment_dict["content"],
    )[0]
    comment.save()
    return comment


def add_tag(tag_dict):
    tag = Tag.objects.get_or_create(name=tag_dict["name"])[0]
    for recipe_index in tag_dict["recipe_indices"]:
        recipe = Recipe.objects.all()[recipe_index]
        tag.recipes.add(recipe)
    tag.save()
    return tag


def add_users(users_dict):
    try:
        for user_dict in users_dict:
            add_user(user_dict)

        bob = User.objects.get(username="Bob the chef")
        assert bob.userprofile.bio == "I am yet another chef"
        print("• Users added successfully ✅")
        return True
    except Exception as e:
        error_message = f"Error adding users: {e}"
        print(error_message)
        return False


def add_recipes(recipes_dict):
    try:
        for recipe_dict in recipes_dict:
            add_recipe(recipe_dict)

        tigania = Recipe.objects.get(
            title="Kokkinisti Tigania Manitarion (Greek Mushroom Sauté in Tomato Sauce)"
        )
        assert tigania.user.username == "Marina the home cook"
        print("• Recipes added successfully ✅")
        return True
    except Exception as e:
        error_message = f"Error adding recipes: {e}"
        print(error_message)
        return False


def add_comments(comments_dict):
    try:
        for comment_dict in comments_dict:
            add_comment(comment_dict)

        first_comment = Comment.objects.get(
            content="Whoa! That looks amazing! I'll have to try it out soon."
        )
        assert first_comment.user.username == "Bob the chef"
        print("• Comments added successfully ✅")
        return True
    except Exception as e:
        error_message = f"Error adding comments: {e}"
        print(error_message)
        return False


def add_tags(tags_dict):
    try:
        for tag_dict in tags_dict:
            add_tag(tag_dict)

        greek_tag = Tag.objects.get(name="Greek")
        assert greek_tag.recipes.count() == 3
        print("• Tags added successfully ✅")
        return True
    except Exception as e:
        error_message = f"Error adding tags: {e}"
        print(error_message)
        return False


def clear_database():
    """Delete all existing data from the database."""
    try:
        User.objects.all().delete()
        Recipe.objects.all().delete()
        Tag.objects.all().delete()
        Comment.objects.all().delete()
        print("• Database cleared successfully ✅")
        return True
    except Exception as e:
        error_message = f"Error clearing database: {e}"
        print(error_message)
        return False


if __name__ == "__main__":
    clear_database()

    add_users(users)
    add_recipes(recipes)
    add_comments(comments)
    add_tags(tags)
