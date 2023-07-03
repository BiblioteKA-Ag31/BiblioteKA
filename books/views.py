from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import Book, User

from .serializers import BookSerializer, BookDetailSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class BookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


def perform_create(self, serializer):
    return serializer.save(person=self.request.user)


class BookDetailView(generics.RetrieveUpdateDestroyAPIVIEW):
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
