from django.shortcuts import get_object_or_404, render
from rest_framework import generics
from .models import  Loan

from .serializers import LoanSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated


class LoanView(generics.ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer


def perform_create(self, serializer):
    # copy = Copy.objects.get(user=self.request.user)
    # serializer.save(copy=copy)
    serializer.save(
        user=self.request.user,
    )


class LoanDetailView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]

    queryset = Loan.objects.all()
    serializer_class = LoanSerializer
