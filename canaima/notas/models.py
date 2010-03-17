from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=30)


class Nota(models.Model):
    titulo = models.CharField(max_length=30)
    nota = models.CharField(max_length=500)
    autor=models.ForeignKey(Autor)

