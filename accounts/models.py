from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(null=True, default="avatar.svg")
