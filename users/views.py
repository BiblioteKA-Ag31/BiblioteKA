from rest_framework import generics

from users.permissions import ItsOwnAccount

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import UserSerializer
from users.permissions import IsCollaborator
from django.shortcuts import get_object_or_404
from .serializers import UserBookSerializer
from books.models import Book


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [ItsOwnAccount]

    queryset = User.objects.all()


class UserBookView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    serializer_class = UserBookSerializer

    def perform_create(self, serializer):
        user_instance = get_object_or_404(User, pk=self.request.data["user_id"])
        print(user_instance)
        book_instance = get_object_or_404(Book, pk=self.request.data["book_id"])
        serializer.save(user=user_instance, book=book_instance)
