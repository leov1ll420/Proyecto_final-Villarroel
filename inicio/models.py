from django.db import models

class Motos(models.Model):
    marca= models.CharField(max_length=30)
    descripcion = models.TextField()
    año= models.IntegerField()
    
    def __str__(self):
        return f'{self.pk}-{self.marca}-{self.año}'




