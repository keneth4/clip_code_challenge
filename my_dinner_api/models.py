from django.db import models
from django.db.models.base import Model
from django.db.models.fields import FloatField

class Cliente(models.Model):
    email = models.CharField(max_length=254, primary_key=True)
    nombre = models.CharField(max_length=254)
    domicilio = models.CharField(max_length=512, default=list)
    telefono = models.CharField(max_length=254)

class Platillo(models.Model):
    TIPO_DE_COCINA = (
        ('M', 'Mexicana'),
        ('I', 'Italiana'),
        ('J', 'Japonesa'),
    )

    OPCIONES_DE_ESTATUS = (
        ('D', 'Disponible'),
        ('N', 'No disponible'),
    )

    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=254)
    descripcion = models.CharField(max_length=512)
    precio = models.FloatField()
    tipo = models.CharField(max_length=1, choices=TIPO_DE_COCINA)
    estatus = models.CharField(max_length=1, choices=OPCIONES_DE_ESTATUS)

class Orden(models.Model):
    id = models.BigAutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    timestamp = models.DateTimeField(auto_now_add=True)
    total = FloatField()
    detalle = models.CharField(max_length=4096, default=dict)
