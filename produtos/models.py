from datetime import datetime
from django.db import models

class Produto(models.Model):
    nome =  models.CharField(verbose_name='Nome do produto', max_length=200)
    descricao = models.TextField()
    preco = models.IntegerField()
    email = models.CharField(verbose_name='Email', max_length=200)
    categoria = models.CharField(verbose_name='Categoria', max_length=200)
    foto_produto = models.ImageField(upload_to='fotos/%d/%m/%Y/')
    data_produto = models.DateTimeField(default=datetime.now)