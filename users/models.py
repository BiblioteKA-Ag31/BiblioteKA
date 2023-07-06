
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserBook(models.Model):
    book = models.ForeignKey("books.Book", on_delete=models.CASCADE, related_name="book")
    user = models.ForeignKey("users.User", on_delete=models.CASCADE, related_name="user")

class User(AbstractUser):
    email = models.EmailField(max_length=150)
    books = models.ManyToManyField(
        "books.Book", through="users.UserBook", related_name="users"
    )

    @property
    def is_employee(self):
        return self.is_superuser


