from django import forms 


class BaseMotoFormulario(forms.Form):
    marca= forms.CharField(max_length=30)
    descripcion= forms.CharField(max_length=250)
    año=forms.IntegerField()
    precio=forms.DecimalField(max_digits=10, decimal_places=2)


class CrearMotoFormulario(BaseMotoFormulario):

    ...
    
class EditarMotoFormulario(BaseMotoFormulario):
    ...
