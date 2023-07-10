from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_superuser", "password", "loans_user"]
        read_only_fields = ["id", "loans_user"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"write_only": True},
        }
        depth = 1

    def create(self, validated_data: dict) -> User:
        return User.objects.create_user(
            **validated_data
            | {"is_superuser": validated_data.get("is_superuser", False)}
        )


class UserBookSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "books",
        ]
        read_only_fields = [
            "id",
            "email",
            "username",
            "books",
        ]

    def create(self, validated_data):
        user = validated_data["user"]
        book = validated_data["book"]
        user.books.add(book)
        return user


class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient_list = serializers.ListField()
