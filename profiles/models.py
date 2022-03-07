from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    bio = models.TextField(blank=True)
    profile_pic = models.ImageField(upload_to="profile-pics/%Y/%m/%d/%H/%M", blank=True, null=True)
    following = models.ManyToManyField(User, related_name="following", blank=True)
    location = models.CharField(max_length=255, blank=True)
    joined = models.DateField(auto_now_add=True)
    date_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-date_created']
