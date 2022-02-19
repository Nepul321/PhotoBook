from rest_framework import serializers
from .models import (
    Post
)

from accounts.serializers import UserPublicSerializer

class PostSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    is_owner = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = Post
        fields = ('image', 'caption', 'user', 'date', 'likes', 'is_owner')

    def get_likes(self, obj):
        likes = obj.likes.count()
        return likes

    def get_is_owner(self, obj):
        request = self.context['request']
        is_owner = False
        if request.user == obj.user:
            is_owner = True
        return is_owner