from django import forms

class crearNuevoUsuario(forms.Form):
    nombredeusuario=forms.CharField(label='Nombre de Usuario', max_length=200)
    contrasena=forms.CharField(label='Contrasena', max_length=200)
    contrasenaConfirmada=forms.CharField(label='Confirmar contrasena', max_length=200)
    nombre=forms.CharField(label='Nombre', max_length=200)
    apellido=forms.CharField(label='Apellido', max_length=200)
    numero=forms.CharField(label='Numero de telefono', max_length=200)
    edad=forms.CharField(label='Edad', max_length=200)
    sexo=forms.CharField(label='Sexo', max_length=200)
    
class IniciarSesion(forms.Form):
    nombredeusuario=forms.CharField(label='Nombre de Usuario', max_length=200)
    contrasena=forms.CharField(label='Contrasena', max_length=200)
    
class crearNuevoProducto(forms.Form): 
    nombredeproducto=forms.CharField(label='Nombre de Producto', max_length=200)
    cantidad=forms.CharField(label='Cantidad de productos(stock)', max_length=200)
    precio=forms.CharField(label='Precio del producto', max_length=200)
    iddeusuario_id=forms.CharField(label='Nombre de usuario(vendedor)', max_length=200)
    
class crearNuevoTransaccion(forms.Form): 
    nombredeusuario=forms.CharField(label='Nombre de usuario(comprador)', max_length=200)
    cantidadcomprar=forms.CharField(label='Cantidad por llevar', max_length=200)
