from rest_framework import generics

from users.permissions import ItsOwnAccount

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ItsOwnAccount]

    queryset = User.objects.all()