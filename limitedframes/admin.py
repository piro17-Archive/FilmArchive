from django.contrib import admin
from limitedframes.models import Lifefourcut
# Register your models here.
@admin.register(Lifefourcut)
class PostAdmin(admin.ModelAdmin):
    pass