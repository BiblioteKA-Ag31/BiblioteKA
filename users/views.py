from rest_framework import generics

from users.permissions import IsCollaborator, ItsOwnAccount

from .models import User
from rest_framework_simplejwt.authentication import JWTAuthentication
from .serializers import SendEmailSerializer, UserSerializer
from users.permissions import IsCollaborator
from django.shortcuts import get_object_or_404
from .serializers import UserBookSerializer
from books.models import Book
from rest_framework.views import APIView, Request, Response
from django.core.mail import send_mail
from django.conf import settings


class UserView(generics.CreateAPIView):
    serializer_class = UserSerializer


class UserDetailsView(generics.RetrieveAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator | ItsOwnAccount]
    serializer_class = UserSerializer
    queryset = User.objects.all()


class UserBookView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    serializer_class = UserBookSerializer

    def perform_create(self, serializer):
        user = self.request.user
        book_instance = get_object_or_404(Book, pk=self.kwargs["pk"])
        serializer.save(user=user, book=book_instance)


class SendEmailView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]

    def post(self, request: Request) -> Response:
        serializer = SendEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        send_mail(
            **serializer.validated_data,
            from_email=settings.EMAIL_HOST_USER,
            fail_silently=False
        )

        return Response({"msg": "emails enviados"})
