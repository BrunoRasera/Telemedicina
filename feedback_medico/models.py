from django.db import models
from paciente.models import Paciente
from home.models import Medicos

class Feedback_medico(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    medico = models.ForeignKey(Medicos, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True)
