from django.contrib import admin
from recipes.models import Recipe, Comment, Tag, UserProfile

admin.site.register(UserProfile)
admin.site.register(Recipe)
admin.site.register(Comment)
admin.site.register(Tag)
