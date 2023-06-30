from rest_framework import generics

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer
