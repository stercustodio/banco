from banco.models.conta import Conta
from django.db import models


class Saldo(models.Model):
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    data_credito = models.DateTimeField()
    valor_credito = models.FloatField()
    data_debito = models.DateTimeField()
    valor_debito = models.FloatField()
    saldo_final = models.FloatField()
    

