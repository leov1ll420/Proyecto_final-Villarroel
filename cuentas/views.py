from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy

from cuentas.forms import MiFormCreacion, EdicionPerfil
from cuentas.models import DatosExtra

def login(request):
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
            usuario = formulario.cleaned_data.get('username')
            contra = formulario.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contra)
            django_login(request, user)
            
            DatosExtra.objects.get_or_create(user=request.user)
            
            return redirect('inicio')
    else:
        formulario = AuthenticationForm()

    return render(request, 'cuentas/login.html', {'form_login': formulario})


def registro(request):
    if request.method == 'POST':
        formulario = MiFormCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('login')
    else:
        formulario = MiFormCreacion()

    return render(request, 'cuentas/registro.html', {'form_registro': formulario})


def ver_perfil(request):
    datos_extra = DatosExtra.objects.get(user=request.user)  
    return render(request, 'cuentas/ver_perfil.html', {'datos_extra': datos_extra})



def editar_perfil(request):
    datos_extra = request.user.datosextra
    formulario = EdicionPerfil(instance=request.user, initial={'biografia': datos_extra.biografia, 'avatar': datos_extra.avatar})

    if request.method == 'POST':
        formulario = EdicionPerfil(request.POST, request.FILES, instance=request.user)
        if formulario.is_valid():
            new_biografia = formulario.cleaned_data.get('biografia')
            new_avatar = formulario.cleaned_data.get('avatar')
            
            if new_biografia:
                datos_extra.biografia = new_biografia

            if new_avatar:
                datos_extra.avatar = new_avatar
                
            datos_extra.save()
            formulario.save()
            
            return redirect('editar_perfil')

    return render(request, 'cuentas/editar_perfil.html', {'form_edit_p': formulario})

class CambioPassword(PasswordChangeView):
    template_name = 'cuentas/cambio_password.html'
    success_url = reverse_lazy('editar_perfil')
