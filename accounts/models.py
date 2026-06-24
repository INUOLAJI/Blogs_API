from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    profile_picture = models.ImageField(upload_to="profile/", blank=True, null=True)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
