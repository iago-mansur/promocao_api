from django.db import models

class Promocao(models.Model):
    empresa = models.CharField(max_length=200)
    loja = models.CharField(max_length=200)
    promocao = models.CharField(max_length=500)

    def __str__(self):
        return self.empresa + '_' + self.loja