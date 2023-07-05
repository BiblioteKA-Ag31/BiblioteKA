from django.shortcuts import get_object_or_404, render
from rest_framework import generics, status
from .models import Loan
from .serializers import LoanSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from users.permissions import IsCollaborator
from loans.permissions import HasRented
from users.models import User


class LoanView(generics.CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator, HasRented]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer

    def perform_create(self, serializer):
        user_instance = get_object_or_404(User, pk=self.request.data["user"])
        serializer.save(user=user_instance)


class LoanListView(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


class LoanDetailView(generics.RetrieveUpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsCollaborator]
    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
