from django.db import models
from users.models import User

# Create your models here.
class Type(models.Model):
    name = models.CharField(max_length=50, verbose_name="회사이름")

class Album(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE, related_name='userFor')
    albumphoto = models.ImageField(blank=True,upload_to='albumphoto/',verbose_name="앨범사진", null=True)
    albumvideo = models.FileField(upload_to='albumvideo/', null=True, verbose_name="앨범동영상",blank=True)
    albummemo = models.TextField(verbose_name="앨범메모")
    albumtype = models.ForeignKey(Type,on_delete=models.CASCADE,related_name="typeFor",null=True,blank=True)
    albumlocation = models.CharField(max_length=50,verbose_name="앨범위치", null=True,blank=True,)
    albumdate = models.DateField(verbose_name='앨범날짜', null =True)

    # albumdate = models.DateTimeField()
