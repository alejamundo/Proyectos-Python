from django.db import models

# Create your models here.
class Descarga(models.Model):
    nombre=models.CharField(max_length=50)
    correo=models.CharField(max_length=50)
    juego=models.CharField(max_length=50)
    
    