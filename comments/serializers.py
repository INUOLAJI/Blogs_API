from .models import Comment
from rest_framework import serializers
from accounts.serializers import UserSerializer


class CommentSerializer(serializers.ModelSerializer):
    post = serializers.CharField(source="post.title")
    user = UserSerializer()

    class Meta:
        model=Comment
        fields=["id", "text", "post", "user", "created_at", "updated_at"]
        read_only_fields=["id", "created_at", "updated_at"]