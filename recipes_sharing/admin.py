from django.contrib import admin
from .models import Recipe, UserProfile
# Register your models here.

admin.site.register(Recipe)
admin.site.register(UserProfile)
