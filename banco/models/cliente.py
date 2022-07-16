from django.db import models


class Cliente(models.Model):
    
    nome = models.CharField(max_length=60)
    cpf = models.CharField(max_length=14, unique=True)
    dt_nascimento = models.CharField(max_length=10)
    email = models.CharField(max_length=50)
    endereco = models.CharField(max_length=60)
    celular = models.CharField(max_length=14)
    senha = models.CharField(max_length=6)
        
    def __str__(self):
        return self.nome
