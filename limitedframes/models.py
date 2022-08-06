from django.db import models

# Create your models here.
class Lifefourcut (models.Model):
    lifephotourl = models.URLField()
    lifecontext = models.CharField(max_length=100, null=True)
    lifeid = models.CharField(max_length=50)
    lifepagename = models.CharField(max_length=50, null = True)