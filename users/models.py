from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=150)
    is_superuser = models.BooleanField(default=False)

    books = models.ManyToManyField("books.Book", related_name="users")
 