from django import forms
from recipes.models import Recipe, Comment, Tag

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