from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from profiles.models import Profile

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    is_active = models.BooleanField(default=False)
    username = models.CharField(max_length=255, unique=True)
    password = models.CharField(max_length=255)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', ]

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile(sender, instance=None, created=False, **kwargs):
    if created:
        Profile.objects.create(
            user=instance
        )