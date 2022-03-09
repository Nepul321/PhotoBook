from rest_framework import serializers
from .models import Profile
from accounts.serializers import UserPublicSerializer


class ProfileSerializer(serializers.ModelSerializer):
    user = UserPublicSerializer(read_only=True)
    followers = serializers.SerializerMethodField(read_only=True)
    following = serializers.SerializerMethodField(read_only=True)
    is_following = serializers.SerializerMethodField(read_only=True)
    profile_pic = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Profile
        fields = ('user', 'bio', 'location', 'joined', 'profile_pic',
                  'followers', 'following', 'is_following')

    def get_followers(self, obj):
        return obj.followers.count()

    def get_following(self, obj):
        return obj.user.following.count()

    def get_is_following(self, obj):
        is_following = False
        context = self.context
        request = context.get("request")
        if request:
            user = request.user
            is_following = user in obj.followers.all()

        return is_following

    def get_profile_pic(self, obj):
        image_url = "https://www.w3schools.com/howto/img_avatar.png"
        if obj.profile_pic:
            image_url = obj.profile_pic.url
        return image_url
