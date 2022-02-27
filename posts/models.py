from django.db import models
from base.models import User
from django.db.models import Q

class PostQuerySet(models.QuerySet):
    def feed(self, user):
        followed_users_id = user.following.values_list("user__id", flat=True)
        return self.filter(
            Q(user__id__in=followed_users_id) |
            Q(user=user)
        ).distinct()

    def globalposts(self):
        return self.filter(
            Q(is_private=False)
        ).distinct()

class PostManager(models.Manager):
    def get_queryset(self, *args, **kwargs):
        return PostQuerySet(self.model, using=self._db)

    def get_users_feed(self, user):
        return self.get_queryset().feed(user)

    def get_global_posts(self):
        return self.get_queryset().globalposts()

class Post(models.Model):
    image = models.ImageField(upload_to="posted_images/", blank=True, null=True)
    caption = models.TextField(blank=True)
    is_private = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, related_name="post_likes", blank=True)

    objects = PostManager()

    class Meta:
        ordering = ['-datetime']