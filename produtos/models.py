from django.db import models
from datetime import datetime

class Lista_produtos(models.Model):
    NOME_PRODUTO = models.CharField(max_length=50)
    UNIDADES_VENDIDAS = models.CharField(max_length=50)
    EM_ESTOQUE = models.CharField(max_length=50)
    DATA_EXPIRADA = models.DateField(default=datetime.now, blank=True)


class Categoria_p(models.Model):
    tipo = models.CharField(max_length=50)
