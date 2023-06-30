from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "name", "email", "is_superuser" "password"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(
            **validated_data | {"is_superuser": validated_data.get("is_superuser")}
        )

