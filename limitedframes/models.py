from django.db import models

# Create your models here.
class Lifefourcut (models.Model):
    lifephotourl = models.URLField()
    lifecontext = models.CharField(max_length=100, null=True)
    lifeid = models.CharField(max_length=50)
    lifepagename = models.CharField(max_length=50, null = True)

class Signature (models.Model):
    signaturephotourl = models.URLField(null=True, blank=True)
    signaturephoto = models.URLField(null=True, blank=True)
    signatureurl = models.URLField(null=True, blank=True)
    signaturephotoinfo = models.CharField(max_length=100, null=True,blank=True)
    signatureid = models.CharField(max_length=50,null=True, blank=True)

class Photoism (models.Model):
    photoismphotourl = models.URLField(null=True, blank=True)
    photoismphoto = models.URLField(null=True, blank=True)
    photoismurl = models.URLField(null=True, blank=True)
    photoismphotoinfo = models.CharField(max_length=100, null=True,blank=True)
    photoismid = models.CharField(max_length=50,null=True, blank=True)