from django.db import models
from django.contrib.auth.models import User

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    dia_inicio = models.DateField()
    dia_final = models.DateField()
    horario = models.TimeField()
    cupos_disponibles = models.PositiveIntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="clase_images")

class Servicio(models.Model):
    nombre = models.CharField(max_length=100)
    horario = models.DateTimeField()
    tipo = models.CharField(max_length=50)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to="clase_images")

class Transaccion(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total_pago = models.DecimalField(max_digits=8, decimal_places=2)
    codigo_descuento = models.CharField(max_length=10, blank=True, null=True)
    nombre = models.CharField(max_length=255)
    precio_normal = models.DecimalField(max_digits=8, decimal_places=2)
    descuento_aplicado = models.DecimalField(max_digits=8, decimal_places=2, default=0)