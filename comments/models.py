from django.db import models
from django.conf import settings
from posts.models import Post

User = settings.AUTH_USER_MODEL

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    date = models.DateField(auto_now_add=True)
    datetime = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-datetime']

    @property
    def is_child(self):
        if self.parent is not None:
            return True
        else:
            return False

    def get_children(self):
        if self.is_child:
            return None
        else:
            return Comment.objects.filter(parent=self)

    