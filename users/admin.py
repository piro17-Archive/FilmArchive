from django.contrib import admin
from . import models
from .models import Profile

# Register your models here.
@admin.register(models.User)
class CustomUserAdmin(admin.ModelAdmin):
    pass

admin.site.register(Profile)