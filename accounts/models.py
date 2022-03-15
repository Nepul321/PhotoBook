from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

class UserKey(models.Model):
    key = models.CharField(max_length=1000)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activated = models.BooleanField(default=False)