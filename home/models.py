from django.db import models
from datetime import datetime

class Medicos(models.Model):
    nome_medico = models.CharField(max_length=255)
    crm = models.CharField(max_length=255)
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    data_nascimento = models.DateField()
    telefone = models.CharField(max_length=20)
    endereco = models.TextField(max_length = 300)
    complemento = models.CharField(max_length=255, blank=True)
    bairro = models.CharField(max_length=255)
    cidade = models.CharField(max_length=255)
    estado = models.CharField(max_length=2)
    cep = models.CharField(max_length=10)
    especialidade = models.CharField(max_length=255)
    situacao = models.CharField(max_length=255)
    area_atuacao = models.CharField(max_length=255)
