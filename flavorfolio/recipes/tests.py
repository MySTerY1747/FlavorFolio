from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from recipes.models import UserProfile, Recipe, Tag, Comment
from datetime import datetime


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
        """test user login works"""
        User.objects.create_user(username="testuser", password="testpass")
        response = self.client.post(
            reverse("recipes:login"), {"username": "testuser", "password": "testpass"}
        )
        self.assertRedirects(response, reverse("recipes:index"))
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_user_logout(self):
        """test user logout works"""
        User.objects.create_user(username="testuser", password="testpass")
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("recipes:logout"))
        self.assertRedirects(response, reverse("recipes:index"))
        self.assertFalse(response.wsgi_request.user.is_authenticated)


class RecipeTests(TestCase):
    #  Helper function
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
        """check signed in users can delete their own recipes"""
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
        """check only recipe owners can delete their recipes"""
        User.objects.create_user(username="otheruser", password="testpass")
        # Also create a UserProfile for the other user
        UserProfile.objects.get_or_create(user=User.objects.get(username="otheruser"))
        self.client.login(username="otheruser", password="testpass")
        response = self.client.post(
            reverse("recipes:delete_recipe", args=[self.recipe.id])
        )
        self.assertEqual(response.status_code, 401)
        self.assertTrue(Recipe.objects.filter(id=self.recipe.id).exists())


class ProfileTests(TestCase):
    #  Helper
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        self.profile = UserProfile.objects.create(user=self.user, bio="Original Bio")

    def test_profile_display(self):
        """ "Test user profile page and view work correctly"""
        self.client.login(username="testuser", password="testpass")
        response = self.client.get(reverse("recipes:user_profile"))
        self.assertContains(response, "testuser")
        self.assertContains(response, "Original Bio")

    def test_edit_bio(self):
        """Test that users can edit their bio"""
        self.client.login(username="testuser", password="testpass")
        new_bio = "Updated Bio Content"
        response = self.client.post(reverse("recipes:edit_bio"), {"bio": new_bio})
        self.assertRedirects(response, reverse("recipes:user_profile"))
        updated_profile = UserProfile.objects.get(user=self.user)
        self.assertEqual(updated_profile.bio, new_bio)


class TagTests(TestCase):
    #  Helper
    def setUp(self):
        self.user = User.objects.create_user(username="testuser", password="testpass")
        UserProfile.objects.get_or_create(user=self.user)
        self.client.login(username="testuser", password="testpass")

    def test_add_tag(self):
        """check signed in users can create tag, and it redirects to tag page"""
        response = self.client.post(
            reverse("recipes:add_tag"), {"name": "Newtag".title()}
        )
        self.assertRedirects(response, reverse("recipes:tag", args=["Newtag".title()]))
        self.assertTrue(Tag.objects.filter(name="Newtag".title()).exists())

    def test_add_duplicate_tag(self):
        """test no duplicate tags are created"""
        Tag.objects.create(name="Existingtag".title())
        response = self.client.post(
            reverse("recipes:add_tag"), {"name": "Existingtag".title()}
        )

        if hasattr(response, "context") and "form" in response.context:
            form = response.context["form"]
            self.assertTrue(form.errors)
        else:
            self.assertFalse(Tag.objects.filter(name="Existingtag".title()).count() > 1)

    def test_add_tags_to_recipe(self):
        """test adding new tags to recipes (god this took forever to get working)"""
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
