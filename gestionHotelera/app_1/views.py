from django.shortcuts import render
from django.shortcuts import redirect
from app_1.forms import FormProyecto
from app_1.models import Proyecto


# Create your views here.
def index(request):
    return render(request, 'index.html')

def listadoProyectos(request):
    cliente = Proyecto.objects.all()
    data = {'proyectos': cliente}
    return render(request, 'proyectos.html', data)

def agregarProyecto(request):
    form = FormProyecto()
    if request.method == 'POST':
        form = FormProyecto(request.POST)
        if form.is_valid() :
            form.save()
        return index(request)
    data = {'form' : form}
    return render(request, 'agregarProyecto.html', data)



def eliminarProyecto(request,id):
    cliente = Proyecto.objects.get(id = id)
    cliente.delete()
    return redirect('/proyectos')  

def actualizarProyecto(request,id):
    cliente = Proyecto.objects.get(id = id)
    form = FormProyecto(instance=cliente)
    if request.method == 'POST' :
        form = FormProyecto(request.POST, instance=cliente)
        if form.is_valid() :
            form.save()
        return index(request)
    data ={'form' : form}
    return render(request,'agregarProyecto.html', data)

