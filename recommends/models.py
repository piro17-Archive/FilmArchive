from django.db import models
from users.models import User

# Create your models here.
class Recommend(models.Model):
    RESULT_CHOICES = (
        ('TEMP', 'temp'),
        ('TEST', 'test'),
        ('HI', 'hi'),
    #   ('봄'),
    #   ('여름'),
    #   ('가을'),
    #   ('겨울'),
    #   ('러블리'),
    #   ('개그'),
    #   ('큐티'),
    #   ('청량'),
    #   ('심플'),
    #   ('유니크'),
    #   ('패턴'),
    #   ('커플'),
    #   ('동물'),
    #   ('인물'),
    #   ('캐릭터'),
   )
    postUser = models.ForeignKey(User,on_delete=models.CASCADE, related_name='postUser_name')
    title = models.CharField(max_length=100, verbose_name="제목")
    content = models.TextField(verbose_name="설명")
    keyword = models.CharField(max_length=50, verbose_name="키워드", choices=RESULT_CHOICES)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    #imagefield left
