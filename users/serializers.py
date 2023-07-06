from rest_framework import serializers
from .models import User, UserBook


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "is_superuser", "password", "loans_user"]
        read_only_fields = ["id"]
        extra_kwargs = {
            "password": {"write_only": True},
            "is_superuser": {"write_only": True},
            "loans_user": {"read_only": True}
        }
        depth = 1

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
        return UserBook.objects.create(**validated_data)


class SendEmailSerializer(serializers.Serializer):
    subject = serializers.CharField()
    message = serializers.CharField()
    recipient_list = serializers.ListField()