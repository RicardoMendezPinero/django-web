from django.db import models

# Create your models here.

class Usuarios(models.Model):
    nombredeusuario=models.CharField(max_length=200)
    contrasena=models.CharField(max_length=200)
    nombre=models.CharField(max_length=200)
    apellido=models.CharField(max_length=200)
    numero=models.CharField(max_length=200)
    edad=models.CharField(max_length=200)
    sexo=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombredeusuario
    
class Productos(models.Model):
    nombredeproducto=models.CharField(max_length=200)
    iddeusuario=models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    cantidad=models.CharField(max_length=200)
    precio=models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombredeproducto
    
class Transaccion(models.Model):
    iddeusuario = models.ForeignKey(Usuarios, on_delete=models.CASCADE)
    iddeproducto = models.ForeignKey(Productos, on_delete=models.CASCADE)
    cantidadcomprar = models.IntegerField()
    totalpagado = models.DecimalField(max_digits=10, decimal_places=2)  # Usando DecimalField para valores de dinero
    def save(self, *args, **kwargs):
        # Obtén el precio del producto relacionado
        precio_producto = self.iddeproducto.precio
         # Calcula el total pagado como cantidadcomprar * precio del producto
        self.totalpagado = self.cantidadcomprar * precio_producto
        super(Transaccion, self).save(*args, **kwargs)
    