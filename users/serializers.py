from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_superuser", "password"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"write_only": True},
        }

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(
            **validated_data
            | {"is_superuser": validated_data.get("is_superuser", False)}
        )


class UserBookSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    user_id = serializers.IntegerField()
    book_id = serializers.IntegerField()

    def create(self, validated_data):
        return super().create(validated_data)
