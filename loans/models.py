from django.db import models
from django.utils import timezone
from datetime import timedelta


class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    date_exit = models.DateField(auto_now_add=True)
    date_devolution = models.DateField(null=True)
    returned = models.BooleanField(default=False)
    copies = models.ForeignKey(
        "books.Copy", on_delete=models.CASCADE, related_name="loans_copies"
    )

    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans_user"
    )

    def save(self, *args, **kwargs):
        if not self.date_exit:
            self.date_exit = timezone.now().date()

        date_devolution = self.date_exit + timedelta(days=5)

        while date_devolution.weekday() >= 5:
            date_devolution += timedelta(days=1)

        self.date_devolution = date_devolution
        super(Loan, self).save(*args, **kwargs)
