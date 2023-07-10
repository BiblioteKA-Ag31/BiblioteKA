from rest_framework import serializers
from .models import Loan


class LoanSerializer(serializers.ModelSerializer):
    returned = serializers.BooleanField(required=False)

    class Meta:
        model = Loan
        fields = [
            "id",
            "date_exit",
            "date_devolution",
            "returned",
            "user",
            "copies",
        ]

    def validate(self, attrs):
        if "returned" in attrs:
            instance = getattr(self, "instance", None)
            if instance and instance.returned and not attrs["returned"]:
                raise serializers.ValidationError(
                    "Cannot set returned to False once it's already True."
                )
        return attrs
