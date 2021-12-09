from django.db import models
from django.db.models.base import Model
from django.db.models.fields import FloatField
from django.utils.translation import gettext_lazy as _

class Cliente(models.Model):
    email = models.CharField(max_length=254, primary_key=True)
    nombre = models.CharField(max_length=254)
    domicilio = models.CharField(max_length=512, default=list)
    telefono = models.CharField(max_length=254)

class Platillo(models.Model):
    class TipoDeCocina(models.TextChoices):
        MEXICANA = 'M', _('Mexicana')
        ITALIANA = 'I', _('Italiana')
        JAPONESA = 'J', _('Japonesa')

    class OpcionesDeEstatus(models.TextChoices):
        DISPONIBLE = 'D', _('Disponible')
        NO_DISPONIBLE = 'N', _('No disponible')

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=254)
    descripcion = models.CharField(max_length=512)
    precio = models.FloatField()
    tipo = models.CharField(max_length=1, choices=TipoDeCocina.choices)
    estatus = models.CharField(max_length=1, choices=OpcionesDeEstatus.choices)

class Orden(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    timestamp = models.DateTimeField()
    total = FloatField()
    detalle = models.CharField(max_length=4096, default=dict)
