from django.db import models
from base.models import User

class Post(models.Model):
    image = models.ImageField(upload_to="posted_images/")
    caption = models.TextField(blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    class Meta:
        ordering = ['-datetime']