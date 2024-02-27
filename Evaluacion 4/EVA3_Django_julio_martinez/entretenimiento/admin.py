from django.contrib import admin
from entretenimiento.models import Clase, Servicio, Transaccion

@admin.register(Clase)
class ClaseAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'dia_inicio', 'dia_final', 'horario', 'cupos_disponibles', 'precio')

@admin.register(Servicio)
class ServicioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio','horario','tipo')

@admin.register(Transaccion)
class TransaccionAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'total_pago', 'codigo_descuento')


