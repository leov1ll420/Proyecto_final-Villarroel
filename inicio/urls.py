from django.urls import path
from inicio.views import inicio,about, motos, crear_moto, eliminar, editar,detalle_moto


urlpatterns = [
    path('',inicio, name='inicio'),
    path('motos/',motos, name='motos'),
    path('motos/crear', crear_moto,name='crear_motos'),
    path('motos/<int:motos_id>/detalle/',detalle_moto ,name='detalle_motos'),
    path('motos/<int:motos_id>/eliminar/', eliminar,name='eliminar_motos'),
    path('motos/<int:motos_id>/editar',editar,name='editar_motos'),
    path('inicio/about',about, name='about')
    
]
