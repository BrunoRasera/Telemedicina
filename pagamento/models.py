from django.db import models

class Pagamento(models.Model):
    forma = models.CharField(max_length=100)
    data = models.DateField(blank=True)
    valor = models.FloatField()
    cancelado = models.BinaryField()
    def __str__(self):
        return self.forma