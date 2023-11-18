from django.urls import path
from cuentas.views import login, registro, editar_perfil, CambioPassword
from django.contrib.auth.views import LogoutView
 
urlpatterns = [
    path('login/', login,name='login'),
    path('logout/',LogoutView.as_view(template_name='cuentas/logout.html'),name='logout'),
    path('registro/', registro,name='Registrarse'),
    path('perfil/editar',editar_perfil,name='editar_perfil'),
    path('perfil/editar/password',CambioPassword.as_view(),name='cambio_password'),
]
