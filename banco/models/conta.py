import uuid

from banco.models.cliente import Cliente
from django.db import models


class Conta(models.Model):
    
    cliente = models.OneToOneField(Cliente, on_delete=models.CASCADE, related_name='cliente')
    dt_criacao = models.DateTimeField(auto_now_add=True)
    numero_conta = models.UUIDField(unique=True, editable=False, default=uuid.uuid4, primary_key=True)
    
    def __str__(self):
        return self.cliente.nome
