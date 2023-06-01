from django.db import models

# Create your models here.
class Resgistro(models.Model):
    nombre=models.CharField(max_length=50)
    cedula=models.CharField(max_length=50)
    correo=models.EmailField()
    curso=models.CharField(max_length=50)
    
    
    
    