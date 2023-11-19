from django.urls import path
from automovil.views import ListadoAutos, CrearAutos, EditarAutos, DetalleAutos,EliminarAutos

urlpatterns = [
    path('automoviles/',ListadoAutos.as_view(),name='automoviles'),
    path('automoviles/crear',CrearAutos.as_view(),name='crear_auto'),
    path('automoviles/<int:pk>/',DetalleAutos.as_view(),name='detalle_auto'),
    path('automoviles/<int:pk>/editar/',EditarAutos.as_view(),name='editar_auto'),
    path('automoviles/<int:pk>/eliminar/',EliminarAutos.as_view(),name='eliminar_auto')
]
