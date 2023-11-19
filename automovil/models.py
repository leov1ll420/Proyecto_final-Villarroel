from django.db import models
from ckeditor.fields import RichTextField

class Auto(models.Model):
    marca=models.CharField(max_length=30)
    modelo=models.CharField(max_length=30)  
    descripcion=RichTextField() 
    fecha_creacion=models.DateField()
    imagen = models.ImageField(upload_to='autos', null=True, blank=True)
    
def __str__(self):
    return f'{self.marca}-{self.modelo}'