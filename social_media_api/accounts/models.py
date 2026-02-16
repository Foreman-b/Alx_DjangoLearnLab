from django.db import models
from django.contrib.auth.models import AbstractUser
# from django.settings import User


class User(AbstractUser):
    bio = models.TextField()
    prifile_picture = models.ImageField(upload_to='uploads/profile_picture/')
    followers = models.ManyToManyField(
        "self", 
        symmetrical=False, 
        related_name="following", 
        blank=True)


