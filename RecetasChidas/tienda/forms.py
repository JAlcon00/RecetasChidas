# Archivo para formularios de la capa de presentación
# Aquí se definirán los formularios para productos, categorías, inventario, etc.
# Formularios para productos, categorías, inventario
# Formularios para login y registro de usuario
# Validaciones de campos (precio > 0, cantidad >= 0, etc.)
# Aquí se definen los formularios de la capa de presentación

from django import forms
from tienda.persistence.models import Categoria, Producto, Inventario, Usuario

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre', 'descripcion']

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'categoria', 'tipo', 'dietas', 'preferencia_sabor', 'image_url']

class InventarioForm(forms.ModelForm):
    class Meta:
        model = Inventario
        fields = ['producto', 'cantidad']

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['nombre', 'correo_electronico', 'contrasena', 'tipo_usuario']
