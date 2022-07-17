from datetime import date
from tkinter.filedialog import SaveFileDialog

from banco.models.conta import Conta
from banco.models.transferencia import Transferencia
from django.db import models


class Extrato(models.Model):
    data_consulta = models.DateField(default=date.today)
    conta = models.OneToOneField(Conta, on_delete=models.CASCADE)
    saldo = models.FloatField()
        
    
