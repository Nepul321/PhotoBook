from django.db import models
from base.models import User

class PostQuerySet(models.QuerySet):
    def feed(self):
        qs = self.filter(is_private=False)
        return qs

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)

    def get_users_feed(self):
        return self.get_queryset().feed()

class Post(models.Model):
    image = models.ImageField(upload_to="posted_images/")
    caption = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    objects = PostManager()

    class Meta:
        ordering = ['-datetime']

    @property
    def get_all_users(self):
        posts = self.objects.filter(user__username="admin")
        return posts