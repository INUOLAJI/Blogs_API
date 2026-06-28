from .models import Post
from .serializers import PostSerializer
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from config.permissions import IsAuthorOrReadOnly
from rest_framework.parsers import MultiPartParser, FormParser 

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.select_related("user").all().order_by("-created_at")
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, IsAuthorOrReadOnly]
    
    parser_classes = [MultiPartParser, FormParser] 

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)