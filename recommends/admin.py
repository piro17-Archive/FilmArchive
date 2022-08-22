from django.contrib import admin
from .models import Recommend, Keyword

# Register your models here.
@admin.register(Keyword)
class PostAdmin(admin.ModelAdmin):
    pass


@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    pass