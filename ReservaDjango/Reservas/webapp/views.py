from django.shortcuts import render
from .models import Reservas

# Create your views here.
def index(request):
    return render(request,"index.html")

def canchas(request):
    return render(request,"canchas.html")

def reservar(request):
    if request.method=='POST':
        nombre= request.POST.get("nombre")
        cancha= request.POST.get("cancha")
        fecha= request.POST.get("fecha")
        hora= request.POST.get("hora")
        duracion= request.POST.get("duracion")
        cel= request.POST.get("cel")
        
        reserva=Reservas(nombre=nombre,cancha=cancha,fecha=fecha,hora=hora,duracion=duracion,cel=cel)
        reserva.save()
        return render(request,'reservar.html',{'mensaje':'Se genero una reserva a nombre de: '+nombre})     
    return render(request,"reservar.html")

def reservas(request):
    reservas=Reservas.objects.all()
    datos={'reservas':reservas}
    return render(request,"reservas.html",datos)

def adminn(request):
    return render(request,"admin.site")

