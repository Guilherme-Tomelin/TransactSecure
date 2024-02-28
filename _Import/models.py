from django.db import models

from django.db import models

class TransacaoFinanceira(models.Model):
    banco_origem = models.CharField(max_length=100)
    agencia_origem = models.CharField(max_length=20)
    conta_origem = models.CharField(max_length=20)
    banco_destino = models.CharField(max_length=100)
    agencia_destino = models.CharField(max_length=20)
    conta_destino = models.CharField(max_length=20)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_hora = models.DateTimeField()
