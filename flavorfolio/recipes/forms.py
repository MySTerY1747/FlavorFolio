from django import forms
from recipes.models import Recipe, Comment, Tag, UserProfile
from django.contrib.auth.models import User


class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Enter Recipe Name: ")
    ingredients = forms.CharField(
        widget=forms.Textarea, help_text="Enter Recipe Ingredients: "
    )
    instructions = forms.CharField(
        widget=forms.Textarea, help_text="Enter Instructions: "
    )
    existing_tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select existing tags:",
    )
    new_tags = forms.CharField(
        max_length=255, required=False, help_text="Add new tags (comma-separated):"
    )
    image = forms.ImageField(help_text="Upload Recipe Image: ", required=False)

    class Meta:
        model = Recipe
        fields = ("title", "ingredients", "instructions", "image")


class EditBioForm(forms.ModelForm):
    bio = forms.CharField(max_length=500, widget=forms.Textarea, help_text="Enter New Bio:")

    class Meta:
        model = UserProfile
        fields = ("bio",)


class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)

    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ("username", "email", "password")


class UploadProfilePictureForm(forms.ModelForm):
    image = forms.ImageField(help_text="Upload New Profile Picture: ")

    class Meta:
        model = UserProfile
        fields = ("image",)


class RecipeImageForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ("image",)


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)
        widgets = {
            "content": forms.Textarea(
                attrs={
                    "class": "comment-input",
                    "placeholder": "Write your comment here...",
                }
            ),
        }


class AddTagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ["name"]
        help_texts = {"name": "Enter a new tag name:"}


class AddTagsForm(forms.Form):
    existing_tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
        help_text="Select existing tags:",
    )
    new_tags = forms.CharField(
        max_length=255, required=False, help_text="Add new tags (comma-separated):"
    )
