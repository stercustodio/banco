from datetime import date

from banco.models.conta import Conta
from django.db import models


class Extrato(models.Model):
    data_consulta = models.DateField(default=date.today)
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE)
    saldo = models.FloatField()
        
    
