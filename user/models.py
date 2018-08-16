from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class User(AbstractUser):
    nick_name = models.CharField('昵称', max_length=10)
