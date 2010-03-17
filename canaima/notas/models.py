from django.db import models


class Autor(models.Model):
    name = models.CharField(max_length=30)
    def __unicode__(self):
        return self.name


class Nota(models.Model):
    titulo = models.CharField(max_length=30)
    nota = models.CharField(max_length=500)
    autor=models.ForeignKey(Autor)
    fecha=models.DateField(auto_now=True)
    def __unicode__(self):
        return u'%s %s' % (self.titulo, self.autor)


