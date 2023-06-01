from django.db import models

# Create your models here.
class Reservas(models.Model):
    nombre=models.CharField(max_length=50)
    cancha=models.CharField(max_length=50)
    fecha=models.DateField()
    hora=models.TimeField()
    duracion=models.IntegerField()
    cel=models.CharField(max_length=50)
    
    
    