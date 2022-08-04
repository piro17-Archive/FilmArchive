from django.db import models
from users.models import User

# Create your models here.

class Keyword(models.Model):
    name = models.CharField(max_length=50, verbose_name="추천키워드")


class Recommend(models.Model):
    postUser = models.ForeignKey(User,on_delete=models.CASCADE, related_name='postUser_name')
    title = models.CharField(max_length=100, verbose_name="제목")
    content = models.TextField(verbose_name="설명")
		# 저장경로: MEDIA_ROOT/posts/20220719/xxx.png
    # DB필드: 'MEDIA_URL/posts/20220719/xxx.png'라는 문자열 저장
    recImage = models.ImageField(blank=True, upload_to="recommends/%Y%m%d", verbose_name="추천사진")
    recKeyword = models.ManyToManyField(Keyword, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
