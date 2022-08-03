from django.contrib import admin
from .models import Recommend

# Register your models here.
@admin.register(Recommend)
class RecommendAdmin(admin.ModelAdmin):
    pass