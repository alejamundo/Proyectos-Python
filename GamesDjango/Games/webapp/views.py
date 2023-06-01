from django.shortcuts import render
from .models import Descarga

# Create your views here.
def index(request):
    return render(request,'index.html')
def games(request):
    return render(request,'games.html')
def registro(request):
    if request.method=='POST':
        nombre=request.POST.get("nombre")
        correo=request.POST.get("correo")
        juego=request.POST.get("juego")
        #insert
        descarga=Descarga(nombre=nombre,correo=correo,juego=juego)
        descarga.save()#guardado
        return render(request, 'registro.html', {'mensaje': 'Tu Juego a sido enviado al correo'})     
    return render(request,'registro.html')
def ver(request):
    descargas=Descarga.objects.all()
    context={'descargas': descargas}
    return render(request,'ver.html',context)