from django.db import models
from django.contrib.auth.models import AbstractUser
from PIL import Image

# Create your models here.
class User(AbstractUser):
    # TODO: null=True 이면 안됨! 아이디찾을때 필요.
    name = models.CharField(max_length=50, null=True, verbose_name="이름")
    email = models.CharField(max_length=100, verbose_name="이메일")
    nickname = models.CharField(null=True, max_length=50, verbose_name="닉네임") #default=username 방법???
   
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='profile.svg', upload_to="users/%Y%m%d", blank=True, null=True, verbose_name="프로필사진")

    def __str__(self):
        return f'{self.user.username} Profile'

    # # 큰 사진을 쪼그만한 크기로 저장
    # def save(self):
    #     super().save()

    #     img = Image.open(self.image.path)

    #     if img.height > 300 or img.width > 300:
    #         output_size = (300, 300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)
