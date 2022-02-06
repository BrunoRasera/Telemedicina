from pyexpat import model
from django.db import models
import consulta
from paciente.models import Paciente
from consulta.models import Consulta

class Feedback_consulta(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    consulta = models.ForeignKey(Consulta, on_delete=models.CASCADE)
    feedback = models.TextField(blank=True)