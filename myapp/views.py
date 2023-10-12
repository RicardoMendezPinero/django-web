from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios, Productos, Transaccion
from django.shortcuts import get_object_or_404, render, redirect
from .forms import crearNuevoUsuario, IniciarSesion, crearNuevoProducto, crearNuevoTransaccion
from django.utils.datastructures import MultiValueDictKeyError

def home(request):
    return render(request, 'index.html', {})

def signup(request):
    if request.method=="GET":
        return render(request, 'signup.html', {'form':crearNuevoUsuario() })
    else: 
        Usuarios.objects.create(nombredeusuario=request.POST['nombredeusuario'], contrasena=request.POST['contrasena'], nombre=request.POST['nombre'], apellido=request.POST['apellido'], numero=request.POST['numero'], edad=request.POST['edad'], sexo=request.POST['sexo'])
        usuario=request.POST['nombredeusuario']
        return redirect(f'/ECOMMERCE/login/<str:{usuario}>')

def verproducto(request, nombredeproducto):
    if request.method=="GET":
        return render(request, 'verproducto.html', {'form':crearNuevoTransaccion(), 'productonombre': nombredeproducto})
    else:
        nombredeusuario=request.POST['nombredeusuario']
        existingUser=Usuarios.objects.filter(nombredeusuario=nombredeusuario)
        existingProduct=Productos.objects.filter(nombredeproducto=nombredeproducto)
        product=get_object_or_404(Productos, nombredeproducto=nombredeproducto)
        precioProducto=int(product.precio)
        vendedor=product.iddeusuario
        cantidad=int(request.POST['cantidadcomprar'])
        total=precioProducto*cantidad
        data={'nombre del comprador': existingUser ,'nombredeproducto': nombredeproducto, 'precio del producto':precioProducto, 'cantidad de productos': str(cantidad), 'total a pagar': str(total), 'vendedor': vendedor }
        nombre=nombredeproducto
        comprador=nombredeusuario
        precioproducto=precioProducto
        cantidadproductos=str(cantidad)
        pagar=str(total)
        vendedorproducto=vendedor
        return render(request, 'order.html',{'nombreproducto': nombre, 'comprador': comprador,'precioproducto': precioproducto, 'cantidadproductos':cantidadproductos, 'pagar': pagar, 'vendedorproducto': vendedorproducto })
    
def login(request):
    if request.method=="GET":
        return render(request, 'login.html', {'form': IniciarSesion()})
    else: 
        nombredeusuario=request.POST['nombredeusuario']
        contrasena=request.POST['contrasena']
        existingnombre=Usuarios.objects.filter(nombredeusuario=nombredeusuario).first()
        existingcontrasena=Usuarios.objects.filter(contrasena=contrasena).first()
        if existingnombre and existingcontrasena:
            return redirect(f'/ECOMMERCE/login/<str:{existingnombre}>')
        else: 
            return render(request, 'login.html', {'form': IniciarSesion()})
        
def vender(request):
    if request.method=="GET":
        return render(request, 'vender.html', {'form': crearNuevoProducto()})
    else:
        Productos.objects.create(nombredeproducto=request.POST['nombredeproducto'], cantidad=request.POST['cantidad'], precio=request.POST['precio'], iddeusuario_id=int(request.POST['iddeusuario_id']))
        return redirect('/ECOMMERCE')
        

def logeado(request, username):
        return render(request, 'logeado.html', {})


def homeproductos(request):
    productos=Productos.objects.values()
    data={'message': 'Success', 'productos': list(productos)}
    return JsonResponse(data, safe=False)



