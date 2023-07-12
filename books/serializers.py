from rest_framework import serializers
from .models import Book, Copy
from django.forms.models import model_to_dict


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "availability",
            "author",
            "synopsis",
            "quant_pag",
        ]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class CopySerializer(serializers.ModelSerializer):
    copies = serializers.IntegerField(write_only=True)

    class Meta:
        model = Copy
        fields = ["id", "book_id", "is_available", "copies"]
        extra_kwargs = {
            # "is_available": {"write_only": True},
        }

    def create(self, validated_data):
        number_of_copies = validated_data.pop("copies")
        for copy in range(number_of_copies):
            created_copy = Copy.objects.create(**validated_data)
        return created_copy

    def update(self, instance: Copy, validated_data: dict) -> Copy:
        copy_available = validated_data.pop("is_available", None)
        setattr(instance, "is_available", copy_available)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_available:
            emails = [item.email for item in instance.book.users.all()]
            representation["users_following"] = emails

        return representation
