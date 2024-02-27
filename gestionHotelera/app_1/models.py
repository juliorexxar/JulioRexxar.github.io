from django.db import models

# Create your models here.

class Proyecto(models.Model):
    fechaInicio = models.DateField()
    fechaTermino = models.DateField()
    rut = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    numeroHabitacion = models.IntegerField()
    cantidadClientes = models.IntegerField()