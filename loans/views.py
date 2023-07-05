from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from .models import Loan
from .serializers import LoanSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCollaborator


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class LoanDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
