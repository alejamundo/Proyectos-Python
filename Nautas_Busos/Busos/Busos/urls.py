"""
URL configuration for Busos project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from webapp.views import index,shop_single,shop,ver,about,registro_usuario,registro_admin,compra,elimina,validar_admin,validar_usuario

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index' ),
    path('shop-single/', shop_single, name='shop-single' ),
    path('shop/', shop, name='shop' ),
    path('ver', ver, name='ver' ),
    path('about/', about, name='about' ),
    
    #path  modales
    path('registro_usuario/', registro_usuario, name='registro_usuario' ),
    path('registro_admin/', registro_admin, name='registro_admin' ),
    path('compra/', compra, name='compra' ),
    path('elimina/<int:id>/', elimina, name='elimina'),
    path('validar_usuario/', validar_usuario, name='validar_usuario'),
    path('validar_admin/', validar_admin, name='validar_admin'),
]
