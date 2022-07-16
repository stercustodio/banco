from banco.models.conta import Conta
from django.db import models


class Saldo(models.Model):
    numero_conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    saldo_data = models.DateField()
    saldo_valor = models.FloatField()

