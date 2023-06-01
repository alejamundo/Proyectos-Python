from django.db import models

# Create your models here.

class Pedidos(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    medio_pago = models.CharField(max_length=50)
    total = models.IntegerField()

class Registros_usuarios(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=50)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    contrasena = models.CharField(max_length=50)
    
class Registros_admin(models.Model):
   nombre= models.CharField(max_length=50)
   cargo= models.CharField(max_length=50)
   correo= models.CharField(max_length=50)
   contrasena= models.CharField(max_length=50)
   
   
   