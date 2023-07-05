from django.shortcuts import get_object_or_404, render
from rest_framework import generics

from users.models import User
from .models import Book, Copy

from .serializers import BookSerializer, BookDetailSerializer, CopySerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCollaborator


class BookView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        return serializer.save(person=self.request.user)


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Book.objects.all()
    serializer_class = BookDetailSerializer
    lookup_url_kwarg = "user_id"

    def get_queryset(self):
        user = self.kwargs["user_id"]
        queryset = super().get_queryset()
        instance_user = get_object_or_404(User, pk=self.kwargs.get("user_id"))

        return queryset.filter(users=instance_user)


class CopyView(generics.ListCreateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    def perform_create(self, serializer):
        instance_book = get_object_or_404(Book, pk=self.kwargs.get("id"))
        serializer.save(book=instance_book)


class CopyDetailsView(generics.RetrieveUpdateAPIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsAuthenticated]

    queryset = Copy.objects.all()
    serializer_class = CopySerializer

    

