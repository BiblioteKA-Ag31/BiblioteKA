from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(max_length=150)
    books = models.ManyToManyField(
        "books.Book",
        related_name="users",
    )

    @property
    def is_employee(self):
        return self.is_superuser
