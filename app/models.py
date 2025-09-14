from django.db import models

class Avaliacao(models.Model):
    nomemusica = models.CharField(max_length=100)
    estrelas = models.IntegerField()
    descricao = models.TextField(max_length=100)

    class Meta:
        verbose_name_plural = "Avaliações"

    def __str__(self):
        return self.nomemusica
    
class Favoritas(models.Model):
    artista = models.CharField(max_length= 80)
    musica = models.CharField(max_length= 100)
