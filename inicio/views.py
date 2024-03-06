from django.shortcuts import render, redirect
from inicio.models import Motos
from inicio.forms import CrearMotoFormulario, EditarMotoFormulario
from django.contrib.auth.decorators import login_required


def inicio(request):
    
    return render(request,'inicio/inicio.html',{})


def about(request):
    
    return render(request,'inicio/about.html',{})


def motos(request):
    marca_a_buscar=request.GET.get('marca')
    if marca_a_buscar:
        lista_de_motos= Motos.objects.filter(marca__icontains=marca_a_buscar)
    else:
        lista_de_motos= Motos.objects.all()

    
    return render(request, 'inicio/motos.html',{'lista_de_motos':lista_de_motos})

def crear_moto(request):
    
    if request.method== 'POST':
        formulario = CrearMotoFormulario(request.POST)
        if formulario.is_valid():
            info_limpia=formulario.cleaned_data
            
            marcaMoto=info_limpia.get('marca')
            descripcionMoto=info_limpia.get('descripcion')
            añoMoto=info_limpia.get('año')
            
            
            moto=Motos(marca=marcaMoto.lower(), descripcion=descripcionMoto, año=añoMoto)
            moto.save()

            
            return redirect('motos')
        else:
            return render(request, 'inicio/crear_motos.html', {'formulario':formulario})
    formulario = CrearMotoFormulario()
    return render(request,'inicio/crear_motos.html',{'formulario':formulario})


@login_required
def eliminar(request,motos_id):
    moto_a_eliminar=Motos.objects.get(id=motos_id)
    moto_a_eliminar.delete()
    return redirect('motos')

@login_required    
def editar(request,motos_id):
    moto_a_editar= Motos.objects.get(id=motos_id)
    if request.method =='POST':
        formulario=EditarMotoFormulario(request.POST)
        if formulario.is_valid():
            info_nueva=formulario.cleaned_data
            moto_a_editar.marca=info_nueva.get('marca')
            moto_a_editar.descripcion=info_nueva.get('descripcion')
            moto_a_editar.año=info_nueva.get('año')
            
            moto_a_editar.save()
            return redirect('motos')
        return render(request,'inicio/editar_motos.html',{'formulario':formulario})
    
    formulario=EditarMotoFormulario(initial={'marca':moto_a_editar.marca,'descripcion':moto_a_editar.descripcion,'año':moto_a_editar.año})
    return render(request,'inicio/editar_motos.html',{'formulario':formulario})

def detalle_moto(request,motos_id):
    moto=Motos.objects.get(id=motos_id)
    return render(request,'inicio/detalle_motos.html',{'moto':moto})
