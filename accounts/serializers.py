from rest_framework import serializers
from base.models import User

class UserPublicSerializer(serializers.ModelSerializer):
    username = serializers.CharField(required=False, allow_blank=True, read_only=True)
    profile_pic_url = serializers.SerializerMethodField(read_only=True)
    class Meta:
        model = User
        fields = [
            'username',  
            'name',
            'profile_pic_url'
        ]

    def get_profile_pic_url(self, obj):
        image_url = None
        if obj.profile.profile_pic:
            image_url = obj.profile.profile_pic.url
        return image_url