# from banco.models.conta import Conta
# from banco.models.transferencia import Transferencia
# from django.db import models
# from django.db.models import Sum


# class Saldo(models.Model):
#     conta_cliente = models.ForeignKey(Conta, on_delete=models.CASCADE)
#     movimentacao_conta = models.ForeignKey(Transferencia, on_delete=models.CASCADE)
    
#     @property
#     def saldo_resultado(self):
        
#         entrada = Transferencia.objects.filter(
#             conta_destino__numero_conta=self.conta_cliente,
#         ).aggregate(total=Sum('valor_transferencia'))

#         saida = Transferencia.objects.filter(
#             conta_origem__numero_conta=self.conta_cliente,
#         ).aggregate(total=Sum('valor_transferencia'))
        
#         credito = entrada.get('total')
#         credito = credito if credito is not None else 0
#         debito = saida.get('total')
#         debito = debito if debito is not None else 0
        
#         resultado = credito -debito
        
#         return resultado
    

    