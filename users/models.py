from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    # TODO: null=True 이면 안됨! 아이디찾을때 필요.
    name = models.CharField(max_length=50, null=True, verbose_name="이름")
    email = models.CharField(max_length=100, verbose_name="이메일")
    nickname = models.CharField(null=True, max_length=50, verbose_name="닉네임") #default=username 방법???
    
   