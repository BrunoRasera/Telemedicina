from django.db import models
from paciente.models import Paciente

class Forma_pagamento(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=255)
    numero_cartao = models.CharField(max_length=50, blank=True)
    data_validade = models.CharField(max_length=20, blank=True)
    nome_cartao = models.CharField(max_length=255, blank=True)

