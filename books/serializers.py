from rest_framework import serializers
from .models import Book, Copy


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
            "quant_copies",
        ]

    def create(self, validated_data):
        return Book.objects.create(**validated_data)


class BookDetailSerializer(serializers.ModelSerializer):
    # books = BookSerializer(many=True)

    class Meta:
        model = Book
        fields = [
            "id",
            "title",
            "availability",
            "author",
            "synopsis",
            "quant_pag",
            # "books",
        ]


class CopySerializer(serializers.ModelSerializer):
    class Meta:
        model = Copy
        fields = [
            "id",
            "book_id",
            "is_available",
        ]

    def create(self, validated_data):
        return Copy.objects.create(**validated_data)

    def update(self, instance: Copy, validated_data: dict) -> Copy:
        copy_available = validated_data.pop("is_available", None)
        setattr(instance, "is_available", copy_available)
        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.is_available:
            emails = [item.email for item in instance.book.users.all()]
            representation["emails"] = emails
        return representation
