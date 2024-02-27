from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from entretenimiento.models import Clase, Servicio, Transaccion
from entretenimiento.forms import TransaccionForm
from datetime import datetime
from decimal import Decimal
from django.contrib.auth.models import User


def home(request):
    return render(request, 'home.html')


def clases(request):
    clases = Clase.objects.all()
    return render(request, 'clases.html', {'clases': clases})


def servicios(request):
    servicios = Servicio.objects.all()
    return render(request, 'servicio.html', {'servicios': servicios})


def reservar_clase(request, clase_id):
    clase = get_object_or_404(Clase, id=clase_id)

    if request.method == 'POST':
        form = TransaccionForm(request.POST, request.FILES)
        if form.is_valid():
            usuario, created = User.objects.get_or_create(
            username=request.user.username)
            total_pago = clase.precio
            codigo_descuento = form.cleaned_data.get('codigo_descuento')
            precio_normal = clase.precio
            descuento_aplicado = 0
            if codigo_descuento == datetime.now().strftime("%d%m%Y"):
                descuento_aplicado = Decimal('0.2') * precio_normal
                total_pago -= descuento_aplicado

            if clase.cupos_disponibles > 0:
                clase.cupos_disponibles -= 1
                clase.save()

                transaccion = Transaccion.objects.create(
                    usuario=usuario,
                    total_pago=total_pago,
                    codigo_descuento=codigo_descuento,
                    nombre=clase.nombre,
                    precio_normal=precio_normal,
                    descuento_aplicado=descuento_aplicado,
                )
                return redirect('pago_exitoso', transaccion_id=transaccion.id)
            else:
                return render(request, 'cupos_agotados.html')
    else:
        form = TransaccionForm()
    return render(request, 'reservar_clase.html', {'clase': clase, 'form': form})


def reservar_servicio(request, servicio_id):
    servicio = get_object_or_404(Servicio, id=servicio_id)

    if request.method == 'POST':
        form = TransaccionForm(request.POST, request.FILES)
        if form.is_valid():
            usuario, created = User.objects.get_or_create(
            username=request.user.username)
            total_pago = servicio.precio
            codigo_descuento = form.cleaned_data.get('codigo_descuento')
            precio_normal = servicio.precio
            descuento_aplicado = 0
            if codigo_descuento == datetime.now().strftime("%d%m%Y"):
                descuento_aplicado = Decimal('0.2') * precio_normal
                total_pago -= descuento_aplicado

            transaccion = Transaccion.objects.create(
                usuario=usuario,
                total_pago=total_pago,
                codigo_descuento=codigo_descuento,
                nombre=servicio.nombre,
                precio_normal=precio_normal,
                descuento_aplicado=descuento_aplicado,
            )
            return redirect('pago_exitoso', transaccion_id=transaccion.id)

    else:
        form = TransaccionForm()

    return render(request, 'reservar_servicio.html', {'servicio': servicio, 'form': form})


def pago_exitoso(request, transaccion_id):
    try:
        transaccion = Transaccion.objects.get(id=transaccion_id)
        descuento_aplicado = transaccion.precio_normal - transaccion.total_pago
        precio_normal = transaccion.precio_normal

        return render(request, 'pago_exitoso.html', {
            'transaccion': transaccion,
            'descuento_aplicado': descuento_aplicado,
            'precio_normal': precio_normal,
        })
    except Transaccion.DoesNotExist:
        raise Http404("La transacción no se encuentra.")


def comprobante_pago(request):
    # Lógica de la vista
    return render(request, 'comprobante_pago.html')
