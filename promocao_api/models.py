from django.db import models

class Promocao(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome
    
class Empresa(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome

class Loja(models.Model):
    nome = models.CharField(max_length=200)

    def __str__(self):
        return self.nome