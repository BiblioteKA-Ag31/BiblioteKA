from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=50)
    availability = models.BooleanField(default=True)
    author = models.CharField(max_length=50)
    synopsis = models.CharField(max_length=150)
    quant_pag = models.IntegerField()


class Copy(models.Model):
    book = models.ForeignKey(
        "books.Book", on_delete=models.CASCADE, related_name="copies_book"
    )
