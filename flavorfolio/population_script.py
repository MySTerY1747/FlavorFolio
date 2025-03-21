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
        "image_path": "population_script_images/rob.jpg",
    },
    {
        "username": "Bob the chef",
        "email": "chefbob@email.com",
        "bio": "I am yet another chef",
        "image_path": "population_script_images/bob.jpg",
    },
    {
        "username": "Marina the home cook",
        "email": "marina@someemail.com",
        "bio": "I am a home cook",
        "image_path": "population_script_images/marina.jpg",
    },
    # New users
    {
        "username": "Dimitri",
        "email": "dimitri@greekfood.com",
        "bio": "Greek cuisine enthusiast sharing traditional family recipes",
        "image_path": "population_script_images/dimitri.jpg",
    },
    {
        "username": "FoodieAlex",
        "email": "alex@foodblog.com",
        "bio": "Exploring culinary traditions from around the Mediterranean",
        "image_path": "population_script_images/alex.jpg",
    },
    {
        "username": "VeganChef",
        "email": "veganchef@greens.com",
        "bio": "Creating plant-based versions of classic recipes",
        "image_path": "population_script_images/veganchef.jpg",
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
    {
        "user_index": 3,
        "title": "Youvetsi (Greek Chicken and Orzo Bake)",
        "ingredients": "- 1.5kg chicken thigh\n - Olive oil\n - 1 onion\n - Thyme\n - Cinnamon\n - Bay leaf\n - 300 grams orzo pasta (kritharaki)\n - Tomato purée\n - Red wine\n - Water\n - Sugar\n - Salt\n - Pepper\n - 1 chicken stock cube (optional)",
        "instructions": "- Season chicken thighs with salt, pepper, and olive oil.\n - Brown the chicken in a pan for a few minutes.\n - Finely chop an onion.\n - Preheat the oven to 180°C.\n - Fry the onion in a pot with olive oil.\n - Add the spices, orzo pasta, and plenty of olive oil to prevent sticking.\n - Set aside the browned chicken.\n - Add tomato purée to the pot.\n - Add wine, water, salt, pepper, stock cube, remaining purée, and sugar.\n - Pour the contents into a baking tray, place chicken thighs on top, drizzle with olive oil.\n - Bake for 30 minutes covered with aluminum foil.\n - Bake for an additional 20 minutes without the foil.",
        "image_path": "population_script_images/giouvetsi.png",
    },
    {
        "user_index": 4,
        "title": "Lemon Chicken with Potatoes",
        "ingredients": "- Chicken thighs\n - Potatoes\n - Olive oil\n - Water\n - Juice from one or two lemons\n - Mustard\n - Honey\n - Thyme\n - Salt\n - Pepper",
        "instructions": "- Cut the chicken thighs into two pieces.\n - Season with salt and pepper.\n - Place them in a pan with olive oil.\n - Simultaneously put the potatoes in the oven.\n - Remove the chicken from the pan, discard the saturated fat, return chicken with fresh olive oil.\n - Add a little water to the pan.\n - Pour in the juice from one or two lemons.\n - Spread mustard and a little honey on top of the chicken.\n - Add salt, pepper, and thyme.\n - Cover and cook on low heat for 30 minutes.",
        "image_path": "population_script_images/kotopoulo-lemonato.jpg",
    },
    {
        "user_index": 0,
        "title": "Moshari Kokkinisto (Greek Style Braised Beef)",
        "ingredients": "- Beef (rump, shoulder, or similar cut)\n - Carrot\n - Onion\n - Garlic\n - Tomatoes\n - Flour\n - Salt\n - Pepper\n - Red wine\n - Tomato paste\n - Various spices",
        "instructions": "- Cut the beef into pieces.\n - Season with salt and coat with flour.\n - Fry briefly until browned.\n - In a pot, add onion, carrot, salt, garlic, wine, and tomato paste.\n - Add your preferred spices.\n - Add the meat to the pot.\n - Cover and simmer on low heat for 1.5 hours.",
        "image_path": "population_script_images/moshari-kokkinisto.jpg",
    },
    {
        "user_index": 5,
        "title": "Vegetarian Bean Burritos",
        "ingredients": "- Tortillas\n - Beans\n - 1 onion\n - 3 cloves garlic\n - Tomatoes (whole or paste)\n - Rice\n - Lemon",
        "instructions": "- Sauté chopped onion and garlic until golden.\n - Add your preferred spices.\n - Add tomatoes, beans, and rice.\n - Place this mixture in a tortilla.\n - Add any vegetables, tofu, or other ingredients you like, plus a squeeze of lemon.\n - Fold properly.\n - For extra flavor, try adding cheese inside and baking in the oven at 180°C for 5 minutes.",
        "image_path": "population_script_images/bean-burritos.jpg",
    },
    {
        "user_index": 1,
        "title": "Mushroom Risotto",
        "ingredients": "- 500g+ mushrooms\n - 1 onion\n - 1 clove garlic\n - 350+ grams Arborio rice\n - White wine\n - 1 vegetable stock cube\n - Butter\n - Parmesan cheese\n - Water",
        "instructions": "- Blend the mushrooms in a blender until finely chopped.\n - Cook them in a saucepan with olive oil, salt, and pepper until moisture evaporates.\n - Chop an onion and caramelize it in a pot with a little garlic.\n - Add the rice and sauté.\n - Pour in white wine and wait for it to evaporate.\n - Add the stock cube and 100ml of hot water.\n - Once water evaporates, add another 100ml, repeating for 10 minutes.\n - Stir in butter and Parmesan cheese.\n - Pan-fry some mushrooms separately for garnish.",
        "image_path": "population_script_images/mushroom-risotto.jpg",
    },
    {
        "user_index": 3,
        "title": "Tigania (Greek Pork Pan Fry)",
        "ingredients": "- Pork neck (800g)\n - Olive oil\n - One clove of garlic\n - White wine (250g)\n - Water (200g)\n - Juice from one lemon\n - Oregano\n - Mustard\n - Honey\n - Salt\n - Pepper\n - French fries",
        "instructions": "- Cut the pork neck into small pieces OF EQUAL SIZE.\n - Add plenty of oil to a large pan or pot.\n - Add salt and pepper.\n - DO NOT TURN THE MEAT except once or twice.\n - Add finely chopped garlic.\n - Pour in the wine and lemon juice.\n - After a minute, add water and close the lid.\n - Cook on LOW HEAT for 35-40 minutes.\n - Turn heat high again.\n - Add a large amount of oregano, mustard, and honey.\n - Stir.\n - Leave for two minutes.\n - Serve with oregano, lemon, and potatoes.",
        "image_path": "population_script_images/tigania.jpg",
    },
    {
        "user_index": 4,
        "title": "Lemony Pork Chops (Petrezikis Style)",
        "ingredients": "- Pork chops\n - Salt and pepper\n - Potatoes\n - Mustard\n - Lemons\n - Rosemary\n - Garlic\n - Oregano\n - Olive oil",
        "instructions": "- Season pork chops with salt, pepper, and a little oil.\n - Lightly cook them in a pan until they get some color.\n - Cut a lemon and squeeze the juice into a baking tray.\n - Add oil, mustard, oregano, and 2 cloves of garlic.\n - Cut potatoes into smaller pieces.\n - Add salt and pepper.\n - Mix everything.\n - Cut a lemon into slices.\n - Place 2 lemon slices and some rosemary between pork chops like a sandwich, and tie with string.\n - Cover baking tray with aluminum foil.\n - Bake in a preheated oven at 180°C for 1.5 hours with foil, and another half hour without.",
        "image_path": "population_script_images/lemon-pork-chops.jpg",
    },
]

tags = [
    {
        "name": "Greek",
        "recipe_indices": [0, 1, 2, 3, 4, 5, 8, 9],
    },
    {
        "name": "Vegetarian",
        "recipe_indices": [0, 1, 2, 6],
    },
    {
        "name": "Vegan",
        "recipe_indices": [0, 2, 6],
    },
    {
        "name": "Chicken",
        "recipe_indices": [3, 4],  # Youvetsi and Lemon Chicken
    },
    {
        "name": "Beef",
        "recipe_indices": [5],  # Moshari Kokkinisto
    },
    {
        "name": "Pork",
        "recipe_indices": [8, 9],  # Tigania and Lemony Pork Chops
    },
    {
        "name": "Pasta",
        "recipe_indices": [3],  # Youvetsi (has orzo pasta)
    },
    {
        "name": "Rice",
        "recipe_indices": [6, 7],  # Bean Burritos and Mushroom Risotto
    },
    {
        "name": "Mushrooms",
        "recipe_indices": [2, 7],  # Kokkinisti Tigania Manitarion and Mushroom Risotto
    },
    {
        "name": "Lemon",
        "recipe_indices": [4, 8, 9],  # Lemon Chicken, Tigania, and Lemony Pork Chops
    },
    {
        "name": "Quick Meal",
        "recipe_indices": [1, 6],  # Greek Salad and Bean Burritos
    },
    {
        "name": "Slow Cook",
        "recipe_indices": [
            0,
            3,
            5,
            8,
            9,
        ],  # Fasolada, Youvetsi, Moshari Kokkinisto, Tigania, Lemony Pork Chops
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
    {
        "content": "Made this last night and my family absolutely loved it! The orzo soaked up all the flavors perfectly.",
        "user_index": 4,
        "recipe_index": 3,
    },
    {
        "content": "Could I use chicken breast instead of thighs for this recipe?",
        "user_index": 5,
        "recipe_index": 4,
    },
    {
        "content": "The cinnamon is a game-changer here! Such a wonderful aroma throughout the house while cooking.",
        "user_index": 2,
        "recipe_index": 3,
    },
    {
        "content": "I added some paprika to the beef and it worked really well with the existing flavors.",
        "user_index": 1,
        "recipe_index": 5,
    },
    {
        "content": "How critical is the honey in this recipe? I'm trying to reduce sugar in my diet.",
        "user_index": 5,
        "recipe_index": 7,
    },
    {
        "content": "My rice kept sticking to the bottom of the pan. Any tips for preventing this?",
        "user_index": 3,
        "recipe_index": 8,
    },
    {
        "content": "I used tortilla chips instead of regular tortillas and made nachos with this mixture. Delicious!",
        "user_index": 0,
        "recipe_index": 6,
    },
    {
        "content": "Perfect comfort food for a rainy day. The house smelled amazing!",
        "user_index": 4,
        "recipe_index": 5,
    },
    {
        "content": "I'm Greek and this is exactly how my grandmother makes it! So authentic!",
        "user_index": 3,
        "recipe_index": 7,
    },
    {
        "content": "Could this work with other vegetables added? Thinking of trying with bell peppers.",
        "user_index": 2,
        "recipe_index": 6,
    },
    {
        "content": "The lemon and rosemary combination is absolutely divine. My new favorite!",
        "user_index": 0,
        "recipe_index": 8,
    },
]


def add_user(user_dict):
    user_model = User.objects.get_or_create(
        username=user_dict["username"], email=user_dict["email"]
    )[0]

    with open(user_dict["image_path"], "rb") as f:
        user = UserProfile.objects.get_or_create(
            user=user_model,
            bio=user_dict["bio"],
            picture=File(f, name=os.path.basename(user_dict["image_path"])),
        )[0]

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
        assert greek_tag.recipes.count() == 8
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
