from rest_framework import generics
from .serializers import RegisterSerializer
from rest_framework.permissions import AllowAny
from rest_framework.parsers import MultiPartParser, FormParser 


class RegisterView(generics.CreateAPIView):
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]