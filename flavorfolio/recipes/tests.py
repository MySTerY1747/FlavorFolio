from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.files.uploadedfile import SimpleUploadedFile
from recipes.models import UserProfile, Recipe, Tag, Comment
from datetime import datetime
import os


# Helper function
def add_recipe(title, ingredients="", instructions=""):
    user = User.objects.get_or_create(username="testuser")[0]
    recipe = Recipe.objects.create(
        user=user, title=title, ingredients=ingredients, instructions=instructions
    )
    return recipe


class AuthenticationTests(TestCase):
    def test_user_registration(self):
        """Check that user registration works correctly"""
        data = {
            "username": "newuser",
            "email": "new@example.com",
            "password": "testpass123",
        }
        response = self.client.post(reverse("recipes:register"), data)
        self.assertEqual(response.status_code, 302)
        self.assertTrue(User.objects.filter(username="newuser").exists())
        self.assertTrue(UserProfile.objects.filter(user__username="newuser").exists())

    def test_user_login(self):
        """Test user login works"""
        User.objects.create_user(username="testuser", password="testpass")
        response = self.client.post(
            reverse("recipes:login"), {"username": "testuser", "password": "testpass"}
        )
        self.assertRedirects(response, reverse("recipes:index"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_logout(self):
        """Test user logout works"""
        User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("recipes:logout"))
        self.assertRedirects(response, reverse("recipes:index"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)

    def test_register_with_existing_username(self):
        """Test registration with duplicate username fails"""
        User.objects.create_user(username="existing", password="testpass")
        response = self.client.post(
            reverse("recipes:register"),
            {
                "username": "existing",
                "email": "test@example.com",
                "password": "testpass",
            },
        )
        self.assertEqual(response.status_code, 200)
        self.assertIn(
            "A user with that username already exists.", response.content.decode()
        )


class RecipeTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        UserProfile.objects.get_or_create(user=self.user)
        self.recipe = Recipe.objects.create(
            user=self.user,
            title="Test Recipe",
            ingredients="Test Ingredients",
            instructions="Test Instructions",
        )

    def test_recipe_upload_date(self):
        self.assertEqual(
            datetime.now().strftime("%x"), self.recipe.upload_date.strftime("%x")
        )

    def test_delete_recipe(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("recipes:delete_recipe", args=[self.recipe.id])
        )
        self.assertRedirects(response, reverse("recipes:user_profile"))
        self.assertFalse(Recipe.objects.filter(id=self.recipe.id).exists())

    def test_unauthorized_recipe_deletion(self):
        User.objects.create_user(username="otheruser", password="testpass")
        UserProfile.objects.create(user=User.objects.get(username="otheruser"))
        self.client.login(username="otheruser", password="testpass")
        response = self.client.post(
            reverse("recipes:delete_recipe", args=[self.recipe.id])
        )
        self.assertEqual(response.status_code, 401)
        self.assertTrue(Recipe.objects.filter(id=self.recipe.id).exists())

    def test_upload_recipe_unauthenticated(self):
        response = self.client.get(reverse("recipes:upload_recipe"))
        self.assertRedirects(
            response,
            f"{reverse('recipes:login')}?next={reverse('recipes:upload_recipe')}",
        )

    def test_recipe_str_representation(self):
        self.assertEqual(str(self.recipe), "Test Recipe")

    def test_recipe_default_image(self):
        self.assertTrue(
            os.path.basename(self.recipe.image.name) == "default-recipe.png"
        )


class ProfileTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = UserProfile.objects.create(user=self.user, bio="Original Bio")

    def test_profile_display(self):
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("recipes:user_profile"))
        self.assertContains(response, "testuser")
        self.assertContains(response, "Original Bio")

    def test_edit_bio(self):
        self.client.login(username="testuser", password="testpass")
        new_bio = "Updated Bio Content"
        response = self.client.post(reverse("recipes:edit_bio"), {"bio": new_bio})
        self.assertRedirects(response, reverse("recipes:user_profile"))
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.bio, new_bio)

    def test_profile_picture_upload(self):
        # Create a valid image file
        test_image = SimpleUploadedFile(
            "test.jpg",
            b"GIF87a\x01\x00\x01\x00\x80\x00\x00\x00\x00\x00\xff\xff\xff\x21\xf9\x04\x01\x00\x00\x00\x00\x2c\x00\x00\x00\x00\x01\x00\x01\x00\x00\x02\x02\x44\x01\x00\x3b",
            content_type="image/jpeg",
        )
        self.client.login(username="testuser", password="testpass")
        response = self.client.post(
            reverse("recipes:upload_new_profile_picture"), {"image": test_image}
        )
        self.profile.refresh_from_db()
        self.assertIn("test", self.profile.picture.name)

    def test_anonymous_profile_access(self):
        other_user = User.objects.create_user(username="otheruser", password="testpass")
        UserProfile.objects.create(user=other_user)
        response = self.client.get(reverse("recipes:profile", args=[other_user.id]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "otheruser")


class TagTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        UserProfile.objects.get_or_create(user=self.user)
        self.client.login(username="testuser", password="testpass")

    def test_add_tag(self):
        response = self.client.post(
            reverse("recipes:add_tag"), {"name": "Newtag".title()}
        )
        self.assertRedirects(response, reverse("recipes:tag", args=["Newtag".title()]))
        self.assertTrue(Tag.objects.filter(name="Newtag".title()).exists())

    def test_add_duplicate_tag(self):
        tag_name = "Dessert"
        try:
            Tag.objects.create(name=tag_name)
        except:
            pass
        self.assertEqual(Tag.objects.filter(name=tag_name).count(), 1)

    def test_add_tags_to_recipe(self):
        recipe = Recipe.objects.create(user=self.user, title="Test Recipe")
        existing_tag = Tag.objects.create(name="Existingtag".title())
        response = self.client.post(
            reverse("recipes:add_tags", args=[recipe.id]),
            {"existing_tags": [existing_tag.id], "new_tags": "Newtag1, Newtag2"},
        )
        self.assertRedirects(response, reverse("recipes:recipe", args=[recipe.id]))
        recipe.refresh_from_db()
        self.assertEqual(recipe.tag_set.count(), 3)
        self.assertTrue(Tag.objects.filter(name="Newtag1".title()).exists())
        self.assertTrue(Tag.objects.filter(name="Newtag2".title()).exists())

    def test_tag_str_representation(self):
        tag = Tag.objects.create(name="TestTag")
        self.assertEqual(str(tag), "TestTag")


class CommentTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        UserProfile.objects.get_or_create(user=self.user)
        self.recipe = Recipe.objects.create(
            user=self.user,
            title="Test Recipe",
            ingredients="Test Ingredients",
            instructions="Test Instructions",
        )
        self.client.login(username="testuser", password="testpass")

    def test_add_comment(self):
        response = self.client.post(
            reverse("recipes:add_comment", args=[self.recipe.id]),
            {"content": "Test Comment Content"},
        )
        self.assertRedirects(response, reverse("recipes:recipe", args=[self.recipe.id]))
        self.assertTrue(Comment.objects.filter(recipe=self.recipe).exists())

    def test_comment_content(self):
        comment = Comment.objects.create(
            user=self.user, recipe=self.recipe, content="Test Comment"
        )
        response = self.client.get(reverse("recipes:recipe", args=[self.recipe.id]))
        self.assertContains(response, "Test Comment")

    def test_comment_str_representation(self):
        comment = Comment.objects.create(
            user=self.user, recipe=self.recipe, content="Test Comment"
        )
        self.assertEqual(str(comment), "Comment by testuser on Test Recipe")

    def test_add_comment_unauthenticated(self):
        self.client.logout()
        response = self.client.post(
            reverse("recipes:add_comment", args=[self.recipe.id]),
            {"content": "Anonymous Comment"},
        )
        self.assertRedirects(
            response,
            f"{reverse('recipes:login')}?next={reverse('recipes:add_comment', args=[self.recipe.id])}",
        )


class ViewTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.recipe = Recipe.objects.create(
            user=self.user,
            title="Test Recipe",
            ingredients="Test Ingredients",
            instructions="Test Instructions",
        )
        self.tag = Tag.objects.create(name="TestTag")
        self.tag.recipes.add(self.recipe)

    def test_index_view(self):
        response = self.client.get(reverse("recipes:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Recipe")

    def test_search_view(self):
        response = self.client.get(reverse("recipes:search"), {"search_query": "Test"})
        self.assertContains(response, "Test Recipe")

    def test_tag_view(self):
        response = self.client.get(reverse("recipes:tag", args=["TestTag"]))
        self.assertContains(response, "Test Recipe")

    def test_nonexistent_recipe_view(self):
        response = self.client.get(reverse("recipes:recipe", args=[999]))
        self.assertEqual(response.status_code, 404)

    def test_load_recipes_pagination(self):
        for i in range(10):
            Recipe.objects.create(user=self.user, title=f"Recipe {i}")
        response = self.client.get(reverse("recipes:load_recipes", args=[5]))
        self.assertEqual(len(response.context["recipes"]), 5)


class ModelTests(TestCase):
    def test_user_profile_str(self):
        user = User.objects.create_user(username="profiletest")
        profile = UserProfile.objects.create(user=user)
        self.assertEqual(str(profile), "Profile of profiletest")

    def test_user_profile_creation_signal(self):
        # Test through registration view
        self.client.post(
            reverse("recipes:register"),
            {
                "username": "signaluser",
                "email": "test@example.com",
                "password": "testpass",
            },
        )
        self.assertTrue(
            UserProfile.objects.filter(user__username="signaluser").exists()
        )
