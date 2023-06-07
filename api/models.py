from django.db import models

"""Empresa pode ter várias lojas"""
class Empresa(models.Model):
    nome = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Empresa'
        verbose_name_plural = 'Empresas'

    def __str__(self):
        return self.nome


"""Lojas podem ter várias promoções"""
class Loja(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=500)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE) #, related_name="empresa")

    class Meta:
        verbose_name = 'Loja'
        verbose_name_plural = 'Lojas'

    def __str__(self):
        return f'{self.empresa}_{self.nome}'

class Promocao(models.Model):
    nome = models.CharField(max_length=200)
    empresa = models.ForeignKey('Empresa', on_delete=models.CASCADE) #, related_name="empresa")
    loja = models.ForeignKey('Loja', on_delete=models.CASCADE) #, related_name="loja")

    class Meta:
        verbose_name = 'Promoção'
        verbose_name_plural = 'Promoções'

    def __str__(self):
        return f'{self.empresa}_{self.loja}: {self.nome}'