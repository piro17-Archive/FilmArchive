from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    first_name = models.CharField(max_length=50, verbose_name="이름")
    last_name = models.CharField(max_length=30, verbose_name="성")
    nickname = models.CharField(null=True, max_length=50, verbose_name="닉네임") #default=username 방법???
    
   