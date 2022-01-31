from django.db import models

class Paciente(models.Model):
    nome_paciente = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    cpf = models.CharField(max_length=20)
    rg = models.CharField(max_length=20)
    endereco = models.CharField(max_length=200)
    complemento = models.CharField(max_length=200, blank=True)
    bairro = models.CharField(max_length=200)
    cidade = models.CharField(max_length=200)
    estado = models.CharField(max_length=200)
    cep = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    data_nascimento = models.DateField()
    sexo = models.CharField(max_length=50)
    naturalidade =  models.CharField(max_length=200)
    nome_mae = models.CharField(max_length=200)
    contato_emergencial = models.CharField(max_length=200)

