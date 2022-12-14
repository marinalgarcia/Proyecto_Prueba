"""proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from ejemplo.views import (ActualizarPersonas, CargarPersonas, ListarPersonas, BuscarCliente,BuscarClienteApellido, 
                            Mostrar_Inventario, AltaProducto,  ActualizarProducto, AltaProveedores, ListarProveedores)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('personas/', ListarPersonas.as_view()),
    path('personas/cargar',CargarPersonas.as_view()),
    path('personas/actualizar',ActualizarPersonas.as_view()),
    path('personas/actualizar/<int:pk>',ActualizarPersonas.as_view()),
    path('personas/Buscar_Nombre', BuscarCliente.as_view()),
    path('personas/Buscar_Apellido',BuscarClienteApellido.as_view()),
    path('Inventario/', Mostrar_Inventario.as_view()), 
    path('Inventario/alta_producto', AltaProducto.as_view()),  
    path('Inventario/Modificar/<int:Producto>', ActualizarProducto.as_view()),
    path('proveedores/alta', AltaProveedores.as_view()),
    path('proveedores/', ListarProveedores.as_view()),
]
