from django.db import models
from django.utils import timezone
from datetime import timedelta


class Loan(models.Model):
    id = models.AutoField(primary_key=True)
    date_exit = models.DateField(auto_now_add=True)
    date_devolution = models.DateField(null=True)
    returned = models.BooleanField(default=False)
    quant_pag = models.IntegerField()
    # descomentar ao criar o app copys
    copies = models.ForeignKey("books.Copy", on_delete=models.CASCADE, related_name="loans_copies")
    
    user = models.ForeignKey(
        "users.User", on_delete=models.CASCADE, related_name="loans_user"
    )

    def save(self, *args, **kwargs):
        # Cálculo da data de devolução (5 dias úteis a partir da data de saída)(tem que testar)
        if not self.date_exit:
            self.date_exit = timezone.now().date()

        date_devolution = self.date_exit + timedelta(days=5)

        # Verificação se a data de devolução cai em um sábado ou domingo (tem que testar)
        while date_devolution.weekday() >= 5:
            date_devolution += timedelta(days=1)

        self.date_devolution = date_devolution
        super(Loan, self).save(*args, **kwargs)
