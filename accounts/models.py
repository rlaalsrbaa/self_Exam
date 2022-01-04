from django.contrib.auth.models import AbstractUser

# Create your models here.
from django.db import models


class User(AbstractUser):

    first_name = None
    last_name = None
    name = models.CharField('이름', max_length=100)
    class GenderChoices(models.TextChoices):
        MALE = "male", "남성"
        FEMALE = "female", "여성"

    gender = models.CharField('성별', max_length=6, blank=True, choices=GenderChoices.choices)
    avatar = models.ImageField('아바타', blank=True, upload_to="accounts/avatar/%Y/%m/%d",
                               help_text="100px * 100px 크기의 gif/png/jpg 이미지를 업로드해주세요.")
