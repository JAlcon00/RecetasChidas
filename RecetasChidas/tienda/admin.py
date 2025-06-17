from django.contrib import admin
from .models import Categoria, Usuario, Producto, Inventario

# Registrar los modelos en el panel de administración
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    search_fields = ('nombre',)

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'correo_electronico', 'tipo_usuario')
    list_filter = ('tipo_usuario',)
    search_fields = ('nombre', 'correo_electronico')

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio', 'categoria', 'tipo')
    list_filter = ('categoria', 'tipo', 'dietas')
    search_fields = ('nombre', 'descripcion')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_display = ('producto', 'cantidad')
    list_filter = ('producto__categoria',)
    search_fields = ('producto__nombre',)
