from pyexpat import model
from django.db import models
from datetime import datetime
from home.models import Medicos
from paciente.models import Paciente

class Exame(models.Model):
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    descricao = models.CharField(max_length=400, blank=True)
    data_solitacao = models.DateField()
    