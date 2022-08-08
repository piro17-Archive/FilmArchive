from django.contrib import admin
from limitedframes.models import Lifefourcut, Signature,Photoism
# Register your models here.
@admin.register(Lifefourcut)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Signature)
class PostAdmin(admin.ModelAdmin):
    pass

@admin.register(Photoism)
class PostAdmin(admin.ModelAdmin):
    pass