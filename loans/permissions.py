from rest_framework import permissions
from django.shortcuts import get_object_or_404
from users.models import User
from loans.models import Loan


class HasRented(permissions.IsAuthenticated):
    def has_permission(self, request, view):
        user_instance = get_object_or_404(User, pk=request.data["user"])

        queryset = Loan.objects.filter(user=user_instance.id)
        for loan in queryset:
            if not loan.returned:
                return False

        print(queryset)
        return super().has_permission(request, view) and request.user.is_superuser
