from django.shortcuts import render
from .models import Resgistro
from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect
# Create your views here.
def index(request):
    return render(request,'index.html')

def registro(request):
    if request.method=='POST':
        nombre=request.POST.get('nombre')
        cedula=request.POST.get('cedula')
        correo=request.POST.get('correo')
        curso=request.POST.get('curso')
        
        registro=Resgistro(nombre=nombre,cedula=cedula,correo=correo,curso=curso)
        registro.save()
        
        
        messages.success(request, 'Registro exitoso')

    return render(request,'index.html') 

def login(request):
    if request.method=='POST':
        usuario=request.POST.get('usuario')
        pwd=request.POST.get('pwd')
        if usuario=="Alejandra" and pwd=="123":
            messages.success(request, 'Bienvenida Alejandra')
            context={'usuario':usuario}
            return render(request,'inscriptos.html',context)
        elif usuario=="Andrea" and pwd=="123":
            messages.success(request, 'Bienvenida Andrea')
            context={'usuario':usuario}
            return render(request,'inscriptos.html',context)
        else:
            messages.success(request, 'Usuario administrador no valido')
            return render(request,'index.html')
           
def inscriptos(request):
    registros=Resgistro.objects.all()
    context={'registros':registros}
    return render(request,'inscriptos.html',context)
    
def elimina(request,id):
    registro = get_object_or_404(Resgistro, pk=id)
    registro.delete()
    return redirect('inscriptos')
        
        
        