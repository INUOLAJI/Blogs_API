from rest_framework import serializers
from .models import Like
from accounts.serializers import UserSerializer
from posts.models import Post

class LikeSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True)
    
    post = serializers.CharField(source="post.title", read_only=True)
    
    post_id = serializers.PrimaryKeyRelatedField(
        queryset=Post.objects.all(),
        source="post", 
        write_only=True
    )

    class Meta:
        model = Like
        fields = ["id", "post", "post_id", "user", "created_at"]
        read_only_fields = ["id", "created_at"]