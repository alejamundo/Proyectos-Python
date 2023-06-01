from django.shortcuts import get_object_or_404, redirect, render
from .models import Registros_usuarios,Registros_admin,Pedidos
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')



def shop_single(request):
    return render(request, 'shop-single.html')
def shop(request):
    return render(request, 'shop.html')
def ver(request):
    pedido=Pedidos.objects.all()
    context={'pedidos': pedido}
    return render(request,'ver.html',context)
    

def registro_usuario(request):
    if request.method=='POST':
       nombre=request.POST.get('nombre')
       direccion=request.POST.get('direccion') 
       correo=request.POST.get('correo')
       telefono=request.POST.get('telefono')
       contrasena=request.POST.get('contrasena')
       
       registro=Registros_usuarios(nombre=nombre,direccion=direccion,correo=correo,telefono=telefono,contrasena=contrasena)
       registro.save()#Almaceno registro del formulario en la bd
       
       messages.success(request, 'Registro exitoso')
    return render(request, 'index.html')

def registro_admin(request):
    if request.method=='POST':
       nombre=request.POST.get('nombre')
       cargo=request.POST.get('cargo') 
       correo=request.POST.get('correo')
       contrasena=request.POST.get('contrasena')
       
       registro=Registros_admin(nombre=nombre,cargo=cargo,correo=correo,contrasena=contrasena)
       registro.save()#Almaceno registro del formulario en la bd
       
       messages.success(request, 'Registro exitoso')
    return render(request, 'ver.html')


def compra(request):
    if request.method=='POST':
       nombre=request.POST.get('nombre')
       direccion=request.POST.get('direccion') 
       telefono=request.POST.get('telefono')
       medio_pago=request.POST.get('medio_pago')
       total=request.POST.get('total')
       
       
       pedido=Pedidos(nombre=nombre,direccion=direccion,telefono=telefono,medio_pago=medio_pago, total=total)
       pedido.save()#Almaceno registro del formulario en la bd
       
       messages.success(request, 'Compra exitoso')
    return render(request, 'shop-single.html')

def elimina(request,id):
    pedido = get_object_or_404(Pedidos, pk=id)
    pedido.delete()
    messages.success(request, 'Pedido Eliminado con exito')
    return redirect('ver')

def validar_usuario(request):
    correo = request.POST.get('correo')
    contrasena = request.POST.get('contrasena')

    try:
        usuario = Registros_usuarios.objects.get(correo=correo, contrasena=contrasena)
        nombre_usuario = usuario.nombre
        return render(request, 'index.html', {'nombre_usuario': nombre_usuario})
    except Registros_usuarios.DoesNotExist:
        nombre_usuario = None
    messages.error(request, 'Usuario no registrado')
    return redirect('index')

    

def validar_admin(request):
    correo = request.POST.get('correo')
    contrasena = request.POST.get('contrasena')

    try:
        usuario = Registros_admin.objects.get(correo=correo, contrasena=contrasena)
        nombre_usuario = usuario.nombre
        cargo_usuario = usuario.cargo
        pedido=Pedidos.objects.all()
        context = {
            'nombre_usuario': nombre_usuario,
            'cargo_usuario': cargo_usuario,
            'pedidos': pedido
        }
        return render(request,'ver.html',context) 
    except Registros_admin.DoesNotExist:
        nombre_usuario = None
        cargo_usuario =None
    messages.error(request, 'Usuario administrador no valido')
    return redirect('index')
   