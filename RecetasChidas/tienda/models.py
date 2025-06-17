# Archivo para modelos de la capa de persistencia
# Los modelos están definidos en persistence/models.py siguiendo la arquitectura por capas
# Este archivo importa todos los modelos para que Django los reconozca

#from .persistence.models import Categoria, Usuario, Producto, Inventario
# Importar los modelos de la capa de persistencia
from .persistence.models import Categoria, Usuario, Producto, Inventario

# Re-exportar todos los modelos para que Django los encuentre
__all__ = ['Categoria', 'Usuario', 'Producto', 'Inventario']
