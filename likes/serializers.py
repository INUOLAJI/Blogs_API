from .models import Like
from rest_framework import serializers
from accounts.serializers import UserSerializer

class LikeSerializer(serializers.ModelSerializer):
    post = serializers.CharField(source="post.title")
    user = UserSerializer()

    class Meta:
        model=Like
        fields=["id", "post", "user", "created_at"]
        read_only_fields=["id", "user", "created_at"]