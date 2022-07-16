from banco.models.conta import Conta
from django.db import models


class Transferencia(models.Model):
      
    conta_origem = models.OneToOneField(Conta, on_delete=models.CASCADE, related_name='conta_origem')
    conta_destino = models.OneToOneField(Conta, on_delete=models.CASCADE, related_name='conta_destino')
    valor_transferencia = models.FloatField()
    data_transferencia = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return (
            self.conta_origem.numero_conta,
            self.conta_destino.numero_conta
        )
