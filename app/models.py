from django.db import models

class Avaliacao(models.Model):
    estrelas = models.IntegerField(max_length=5)
    descricao = models.TextField(max_length=100)
