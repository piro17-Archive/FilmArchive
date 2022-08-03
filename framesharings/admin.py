from django.contrib import admin
from .models import Keyword, Frame
# Register your models here.
@admin.register(Keyword)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Frame)
class PostAdmin(admin.ModelAdmin):
    pass