from django.db import models
    
class Empresa(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Empresa'
        verbose_plural = 'Empresas'

    def __str__(self):
        return self.nome


class Loja(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Loja'
        verbose_plural = 'Lojas'

    def __str__(self):
        return self.nome

class Promocao(models.Model):
    nome = models.CharField(max_length=200)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE)
    loja = models.ForeignKey('Loja', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Promoção'
        verbose_plural = 'Promoções'

    def __str__(self):
        return f'{self.empresa}_{self.loja}: {self.nome}'
"""'.promocao_api.Empresa'"""