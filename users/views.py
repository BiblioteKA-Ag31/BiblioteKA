from rest_framework import generics
from yaml import serialize

from users.permissions import IsCollaborator, ItsOwnAccount

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import SendEmailSerializer, UserSerializer
from users.permissions import IsCollaborator
from django.shortcuts import get_object_or_404
from .serializers import UserBookSerializer
from books.models import Book
from rest_framework.views import APIView
from django.core.mail import send_mail
from django.conf import settings


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator | ItsOwnAccount]

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

class SendEmailView(APIView):
    def post(self, request):
        serialize = SendEmailSerializer(data=request.data)
        serialize.is_valid(raise_exception=True)

        send_mail(
            **serialize.validated_data,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False
        )
        
