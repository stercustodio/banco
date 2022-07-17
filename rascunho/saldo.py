# from banco.models.extrato import Extrato
# from banco.models.transferencia import Transferencia
# from django.db import models


# class Saldo(models.Model):
#     conta = models.ForeignKey(Extrato, on_delete=models.CASCADE)
    
#     @property
#     def entradas():
#         conta = Saldo()
#         return Transferencia.objects.filter(
#         transferencia__conta_destino = conta.conta_consultada).aggregate(fields='valor_transferencia')
    
#     @property        
#     def saidas():
#         conta = Saldo()
#         return Transferencia.objects.filter(
#         transferencia__conta_origem = conta.conta_consultada).aggregate(fields='valor_transferencia')
    
#     @property
#     def saldofinal():
#         return Saldo.entradas() - Saldo.saidas()

#     def __str__(self):
#         return (
#             self.entradas.entradas(),
#             self.saidas.saidas(),
#             self.saldofinal.saldofinal()
#         )
