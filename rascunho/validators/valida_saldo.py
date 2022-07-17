from banco.models.conta import Conta
from banco.models.transferencia import Transferencia
from django.db import models
from django.db.models import Sum


class ValidaSaldo(models.Model):

    conta_instancia = Conta()
    conta = conta_instancia.numero_conta

    @property
    def data_credito(self):
        return Transferencia.objects.get(
            conta_origem__exact=self.conta).get(
                'data_transferencia')
    @property
    def valor_credito(self):
        return Transferencia.objects.get(
            conta_destino__exact=self.conta).get(
                'valor_transferencia')
    @property
    def data_debito(self):
        return Transferencia.objects.get(
            conta_destino__exact=self.conta).get(
                'data_transferencia')
    @property    
    def valor_debito(self):
        return Transferencia.objects.get(
            conta_origem__exact=self.conta).get(
                'valor_transferencia')
    @property
    def saldo_final(self):
        return Sum(self.valor_credito(), self.valor_debito())
            