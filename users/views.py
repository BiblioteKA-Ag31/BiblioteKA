from rest_framework import generics

from users.permissions import IsCollaborator, ItsOwnAccount

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator | ItsOwnAccount]

    queryset = User.objects.all()
    serializer_class = UserSerializer
