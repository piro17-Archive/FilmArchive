from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser,models.Model):
    nickname = models.CharField(null=True, max_length=50, verbose_name="닉네임") #default=username 방법???
    
   