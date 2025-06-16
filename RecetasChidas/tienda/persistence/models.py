from django.db import models

class Categoria(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre

class Usuario(models.Model):
    TIPO_USUARIO = [
        ('cliente', 'Cliente'),
        ('administrador', 'Administrador'),
    ]
    nombre = models.CharField(max_length=100)
    correo_electronico = models.EmailField(max_length=100, unique=True)
    contrasena = models.CharField(max_length=255)
    tipo_usuario = models.CharField(max_length=20, choices=TIPO_USUARIO, default='cliente')

    def __str__(self):
        return self.nombre

class Producto(models.Model):
    TIPO_PRODUCTO = [
        ('comida preparada', 'Comida preparada'),
        ('kit de cocina', 'Kit de cocina'),
    ]
    DIETAS = [
        ('vegana', 'Vegana'),
        ('vegetariana', 'Vegetariana'),
        ('sin gluten', 'Sin gluten'),
        ('sin lactosa', 'Sin lactosa'),
        ('keto', 'Keto'),
    ]
    SABORES = [
        ('salado', 'Salado'),
        ('dulce', 'Dulce'),
        ('picante', 'Picante'),
        ('agridulce', 'Agridulce'),
    ]
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT)
    tipo = models.CharField(max_length=20, choices=TIPO_PRODUCTO)
    dietas = models.CharField(max_length=100, blank=True)
    preferencia_sabor = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.nombre

class Inventario(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} - {self.cantidad}"
from django.db import models