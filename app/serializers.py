from rest_framework import serializers
from .models import User, ImageMaster, PostMaster, CommentMaster


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'first_name', 'last_name', 'profile_picture')


class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ImageMaster
        fields = ('id', 'title', 'description', 'image', 'created_at', 'updated_at')


class PostMasterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostMaster
        fields = ('id', 'user', 'title', 'description', 'image_path', 'created_at')