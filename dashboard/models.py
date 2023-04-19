from django.db import models
from datetime import datetime

class Notificacoes(models.Model):
    vendedor = models.CharField(max_length=120)
    descricao = models.CharField(max_length=120)
    tp_envio = models.CharField(max_length=120)


class Pedidos(models.Model):
    STATUS = models.CharField(max_length=100)
    OPERACAO = models.CharField(max_length=100)
    LOCALIZACAO = models.CharField(max_length=100)
    DISTANCIA = models.CharField(max_length=100)
    DATA_INICIAL = models.DateTimeField(default=datetime.now, blank=True)
    ENDERECO_ENTREGA = models.CharField(max_length=50)

    
