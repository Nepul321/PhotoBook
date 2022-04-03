from rest_framework import serializers
from .models import Comment
from accounts.serializers import UserPublicSerializer
from posts.serializers import PostSerializer


class ChildCommentSeriailzer(serializers.ModelSerializer):
    user = UserPublicSerializer()

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'date')


class CommentSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    post = PostSerializer(read_only=True)
    children = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'user', 'content', 'date', 'datetime', 'post', 'children')

    def get_children(self, obj):
        qs = Comment.objects.filter(parent__pk=obj.pk)
        serializer = ChildCommentSeriailzer(
            qs, many=True, context={"request": self.context['request']})
        return serializer.data

