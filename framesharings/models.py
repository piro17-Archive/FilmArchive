from django.db import models
from users.models import User
# Create your models here.

class Keyword(models.Model):
    name = models.CharField(max_length=50, verbose_name="프레임키워드")

class Frame(models.Model):
    userid = models.ForeignKey(User,on_delete=models.CASCADE, related_name='userframeFor')
    framephoto = models.ImageField(default = None,blank=True,upload_to='framephoto/',verbose_name="프레임사진",null=False)
    frametitle = models.CharField(max_length=50,verbose_name="프레임제목", null=True,blank=True,)
    framekeyword = models.ManyToManyField(Keyword,blank=True)
    frameexample = models.ImageField(blank=True,upload_to='frameexample/',verbose_name="프레임예시", null=True)
    framepublic = models.BooleanField(default=True)
    framememo = models.TextField(verbose_name="프레임메모")
    framelikeuser = models.ManyToManyField(User,blank=True,verbose_name='프레임좋아요수',related_name='likeMany')
    framesaveuser = models.ManyToManyField(User,blank=True,related_name='saveMany')
    framelikedate = models.TextField(blank=True,null=True,default="null", verbose_name="좋아요날짜")
    frameweeklike = models.IntegerField(blank=True,null=True,default=0,verbose_name="주간좋아요수")