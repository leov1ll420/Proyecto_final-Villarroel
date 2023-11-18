from django import forms 


class BaseMotoFormulario(forms.Form):
    marca= forms.CharField(max_length=30)
    descripcion= forms.CharField(max_length=250)
    año=forms.IntegerField()


class CrearMotoFormulario(BaseMotoFormulario):

    ...
    
class EditarMotoFormulario(BaseMotoFormulario):
    ...
