from typing import List, Optional
from tienda.domain.schemas import UsuarioEntity, CategoriaEntity, ProductoEntity
from tienda.persistence.models import Usuario, Categoria, Producto


class CategoriaRepositorio:
    """Repositorio básico para la entidad Categoria."""
    @staticmethod
    def obtener_todas() -> List[CategoriaEntity]:
        categorias = Categoria.objects.all()
        return [
            CategoriaEntity(
                id=categoria.id,
                name=categoria.nombre,
                description=categoria.descripcion
            )
            for categoria in categorias
        ]

class ProductoRepositorio:
    """Repositorio básico para la entidad Producto."""
    @staticmethod
    def obtener_todos() -> List:
        # Método de ejemplo para obtener todos los productos
        productos = Producto.objects.all()
        return [
            ProductoEntity(
                id=producto.id,
                name=producto.nombre,
                description=producto.descripcion,
                price=producto.precio,
                category=CategoriaEntity(
                    id=producto.categoria.id,
                    name=producto.categoria.nombre,
                    description=producto.categoria.descripcion
                ),
                type=producto.tipo,
                diets=producto.dietas.split(',') if producto.dietas else [],
                flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
                image_url=producto.image_url
            )
            for producto in productos
        ]
    
    def obtener_producto_por_id(producto_id: int) -> Optional[ProductoEntity]:
        try:
            producto = Producto.objects.get(id=producto_id)
            return ProductoEntity(
                id=producto.id,
                name=producto.nombre,
                description=producto.descripcion,
                price=producto.precio,
                category=CategoriaEntity(
                    id=producto.categoria.id,
                    name=producto.categoria.nombre,
                    description=producto.categoria.descripcion
                ),
                type=producto.tipo,
                diets=producto.dietas.split(',') if producto.dietas else [],
                flavors=producto.preferencia_sabor.split(',') if producto.preferencia_sabor else [],
                image_url=producto.image_url
            )
        except Producto.DoesNotExist:
            return None

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
