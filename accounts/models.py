from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUser(AbstractUser):
    bio = models.TextField(null=True, blank=True)
    avatar = models.ImageField(
        blank=True, upload_to="profile/", default="images/profile/avatar_rwpw3x"
    )


# hsnvshjfjfh84365287958mnd$#?
