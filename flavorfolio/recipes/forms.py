from django import forms
from recipes.models import Recipe, Comment, Tag, UserProfile
from django.contrib.auth.models import User

class RecipeForm(forms.ModelForm):
    title = forms.CharField(max_length=128,
                           help_text="Enter Recipe Name: ")
    
    ingredients = forms.CharField(widget=forms.Textarea,
                                  help_text="Enter Recipe Ingredients: ")
    
    instructions = forms.CharField(widget=forms.Textarea,
                                   help_text="Enter Instructions: ")
    
    tags = forms.CharField(widget=forms.Textarea,
                                   help_text="Enter Recipe Tags (separated by commas): ")
    
    image = forms.ImageField(help_text="Upload Recipe Image: ",
                             required=False)

    class Meta:
        model = Recipe
        fields = ('title', 'ingredients', 'instructions','tags','image')

class EditBioForm(forms.ModelForm):
    bio = forms.CharField(widget=forms.Textarea,
                          help_text="Enter New Bio:")

    class Meta:
        model = UserProfile
        fields = ('bio',)

class RegistrationForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')

class UploadProfilePictureForm(forms.ModelForm):
    image = forms.ImageField(help_text="Upload New Profile Picture: ")

    class Meta:
        model = UserProfile
        fields = ('image',)
