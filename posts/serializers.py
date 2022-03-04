from rest_framework import serializers
from .models import (
    Post
)

from accounts.serializers import UserPublicSerializer

POST_VALIDATE = ['like', 'unlike']

class PostSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    likes = serializers.SerializerMethodField(read_only=True)
    is_owner = serializers.SerializerMethodField(read_only=True)
    # image = serializers.ImageField()
    class Meta:
        model = Post
        fields = ('id', 'image', 'caption', 'user', 'date', 'likes', 'is_owner', 'is_private')

    def get_likes(self, obj):
        likes = obj.likes.count()
        return likes

    def get_is_owner(self, obj):
        request = self.context['request']
        is_owner = False
        if request.user == obj.user:
            is_owner = True
        return is_owner

class PostActionSerializer(serializers.Serializer):
    id = serializers.CharField()
    action = serializers.CharField()
    def validate_action(self, value):
        value = value.lower().strip()
        if value not in POST_VALIDATE:
            raise serializers.ValidationError("This is not a valid action")
        return value    