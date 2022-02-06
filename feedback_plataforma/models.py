from django.db import models
from home.models import Medicos
from paciente.models import Paciente

class feedback_plataforma(models.Model):
    feedack = models.TextField(max_length=500, blank=True)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)