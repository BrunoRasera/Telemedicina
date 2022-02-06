from django.db import models
from datetime import datetime
from home.models import Medicos
from paciente.models import Paciente
from pagamento.models import Pagamento

class Consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    pagamento = models.ForeignKey(Pagamento, on_delete=models.CASCADE)
    receita = models.CharField(max_length=400)
    data = models.DateTimeField()
    realizada = models.BinaryField()
    motivo_cancelamento = models.TextField(max_length=500, blank=True)
    