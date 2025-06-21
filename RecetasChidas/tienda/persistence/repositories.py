from tienda.domain.schemas import UsuarioEntity
from tienda.persistence.models import Usuario

class CategoriaRepositorio:
    """Repositorio básico para la entidad Categoria."""
    @staticmethod
    def obtener_todas():
        # Método de ejemplo para obtener todas las categorías
        return []

class ProductoRepositorio:
    """Repositorio básico para la entidad Producto."""
    @staticmethod
    def obtener_todos():
        # Método de ejemplo para obtener todos los productos
        return []

class InventarioRepositorio:
    """Repositorio básico para la entidad Inventario."""
    def __init__(self):
        pass

    def obtener_todos(self):
        # Método de ejemplo para obtener todos los inventarios
        return []

class UsuarioRepositorio:
    """Repositorio básico para la entidad Usuario."""
    def __init__(self):
        pass

    def obtener_todos(self):
        # Método de ejemplo para obtener todos los usuarios
        return []
    
    @staticmethod
    def buscar_por_email_y_password(email, password):
        try:
            user = Usuario.objects.get(correo_electronico=email)
            if user.contrasena == password:
                return UsuarioEntity(
                    id=user.id,
                    nombre=user.nombre,
                    correo_electronico=user.correo_electronico,
                    contrasena='',
                    tipo_usuario=user.tipo_usuario
                )
        except Usuario.DoesNotExist:
            return None
        return None
