from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    class Meta:
        model: Loan
        fields = [
            "id",
            "date_exit",
            "date_devolution",
            "returned",
            "quant_pag",
            "user_id",
            "copies_id"
        ]

        def create(self, validated_data):
            return Loan.objects.create(**validated_data)
