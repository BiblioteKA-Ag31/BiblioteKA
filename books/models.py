from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    author = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=150)
    quant_pag = models.PositiveIntegerField()


class Copy(models.Model):
    is_available = models.BooleanField(default=True)
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies_book"
    )
