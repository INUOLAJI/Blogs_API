from .models import Post
from rest_framework import serializers
from accounts.serializers import UserSerializer


class PostSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    comments_count = serializers.SerializerMethodField(read_only=True)
    likes_count = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Post
        fields = ["id", "title", "contents", "comments_count", "likes_count", "user", "image", "created_at", "updated_at"]
        read_only_fields = ["id", "user", "created_at", "updated_at"]

    def get_comments_count(self, obj):
        return obj.comments.count()

    def get_likes_count(self, obj):
        return obj.likes.count()