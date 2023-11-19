from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from automovil.models import Auto
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin


class ListadoAutos(ListView):
    model = Auto
    context_object_name= 'lista_de_autos'
    template_name= 'automovil/automoviles.html'
    
    
class CrearAutos(CreateView):
    model=Auto
    template_name= 'automovil/crear_auto.html'
    fields=['marca','modelo','descripcion','fecha_creacion', 'imagen']
    success_url=reverse_lazy('automoviles')

class EditarAutos(LoginRequiredMixin,UpdateView):
    model=Auto
    template_name= 'automovil/editar_auto.html'
    fields=['marca','modelo','descripcion','fecha_creacion', 'imagen']
    success_url=reverse_lazy('automoviles')   
    
class DetalleAutos(DetailView):
    model=Auto
    template_name= 'automovil/detalle_auto.html'  

class EliminarAutos(LoginRequiredMixin,DeleteView):
    model=Auto
    template_name= 'automovil/eliminar_auto.html'
    success_url=reverse_lazy('automoviles')    