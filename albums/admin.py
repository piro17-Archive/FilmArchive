from django.contrib import admin
from .models import Album, Type

# Register your models here.
@admin.register(Album)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Type)
class PostAdmin(admin.ModelAdmin):
    pass