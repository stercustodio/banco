from datetime import date

from banco.models.conta import Conta
from django.db import models


class Extrato(models.Model):
    '''Verifica o saldo de uma conta na data especificada'''
    
    data_consulta = models.DateField(default=date.today)
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE)
    saldo = models.FloatField()
        
    # não obtive o resultado esperado
    # deixei salvo algumas tentativas na pasta rascunho    
