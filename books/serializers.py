from rest_framework import serializers
from .models import Book


    
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model: Book
        fields=['title', 'availability','author','synopsis','quant_pag']

        def create(self, validated_data):
            return Book.objects.create_user(**validated_data)

class LivroDetailSerializer(serializers.ModelSerializer):
    books = BookSerializer(many=True)

    class Meta:
        model = Book
        fields = ["id",'title','availability', "author", "synopsis", "quant_pag"]